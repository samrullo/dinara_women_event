import logging
from django.shortcuts import render, redirect
from ..models import QuestionThree
from ..forms import QuestionThreeForm

import logging
from django.shortcuts import render, redirect
from ..models import QuestionThree
from django.conf import settings
import json


def view_question_threes(request):
    col_map_file = settings.BASE_DIR / "data" / "questionnaire_three_en_to_uz.json"
    col_mappings = json.loads(col_map_file.read_text(encoding="utf-8"))
    question_threes = QuestionThree.objects.all().prefetch_related("seminar_topic", "interactive_style")

    columns = ["id", "responder", "seminar_topic", "seminar_topic_other", "interactive_style","comments"]
    columns_translated = [col_mappings[col] if col in col_mappings else col for col in columns]

    logging.debug(f"there are {len(question_threes)} question three records, {question_threes}")

    return render(request, "question_three/data_table.html", {
        "columns": columns_translated,
        "data": question_threes,
        "title": "3-bo'lim. Seminar mavzulari va interaktiv uslublar",
        "edit_view": "edit_question_three",
        "new_view": "create_question_three"
    })


def create_question_three(request):
    if request.method == "POST":
        form = QuestionThreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_threes")

    form = QuestionThreeForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Question Three"})


def edit_question_three(request, pk: int):
    question_three = QuestionThree.objects.get(pk=pk)
    logging.debug(f"found question three : {question_three}, {question_three.seminar_topic_other}")
    if request.method == "POST":
        form = QuestionThreeForm(request.POST, instance=question_three)
        if form.is_valid():
            form.save()
            return redirect("question_threes")

    form = QuestionThreeForm(instance=question_three)
    return render(request, "form_template.html", {"form": form, "title": "Edit Question Three"})
