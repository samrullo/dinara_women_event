import logging
from django.shortcuts import render, redirect
from ..models import QuestionTwo
from ..forms import QuestionTwoForm
from django.conf import settings
import json


def view_question_twos(request):
    col_map_file = settings.BASE_DIR / "data" / "questionnaire_two_en_to_uz.json"
    col_mappings = json.loads(col_map_file.read_text(encoding="utf-8"))
    question_twos = QuestionTwo.objects.all()

    columns = ["id", "responder", "difficulties_in_japan", "difficulties_in_japan_other",
               "your_priority_problem", "use_uzbek_community_help"]
    columns_translated = [col_mappings[col] if col in col_mappings else col for col in columns]

    logging.debug(f"there are {len(question_twos)} question two records, {question_twos}")

    return render(request, "question_two/data_table.html", {
        "columns": columns_translated,
        "data": question_twos,
        "title": "2-bo'lim. Yaponiyaga ko'chib kelish va moslashuv",
        "edit_view": "edit_question_two",
        "new_view": "create_question_two"
    })


def create_question_two(request):
    if request.method == "POST":
        form = QuestionTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_twos")

    form = QuestionTwoForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Question Two"})


def edit_question_two(request, pk: int):
    question_two = QuestionTwo.objects.get(pk=pk)
    logging.debug(f"found question two : {question_two}, {question_two.your_priority_problem}")
    if request.method == "POST":
        form = QuestionTwoForm(request.POST)
        if form.is_valid():
            for field in form.cleaned_data:
                setattr(question_two, field, form.cleaned_data[field])
            question_two.save()
            return redirect("question_twos")

    form = QuestionTwoForm(instance=question_two)
    return render(request, "form_template.html", {"form": form, "title": "Edit Question Two"})
