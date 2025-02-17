import logging
from django.shortcuts import render, redirect
from ..models import QuestionFour
from ..forms import QuestionFourForm


import logging
from django.shortcuts import render, redirect
from ..models import QuestionFour
from django.conf import settings
import json

def view_question_fours(request):
    col_map_file = settings.BASE_DIR / "data" / "questionnaire_four_en_to_uz.json"
    col_mappings = json.loads(col_map_file.read_text(encoding="utf-8"))
    question_fours = QuestionFour.objects.all().prefetch_related("howyoufoundus")

    columns = ["id", "responder", "improvements_for_future", "howyoufoundus", "howyoufoundus_other"]
    columns_translated = [col_mappings[col] if col in col_mappings else col for col in columns]

    logging.debug(f"there are {len(question_fours)} question four records, {question_fours}")

    return render(request, "question_four/data_table.html", {
        "columns": columns_translated,
        "data": question_fours,
        "title": "4-bo'lim. Kelajakda takomillashtirish takliflari",
        "edit_view": "edit_question_four",
        "new_view": "create_question_four"
    })


def create_question_four(request):
    if request.method == "POST":
        form = QuestionFourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_fours")

    form = QuestionFourForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Question Four"})


def edit_question_four(request, pk: int):
    question_four = QuestionFour.objects.get(pk=pk)
    logging.debug(f"found question four : {question_four}, {question_four.improvements_for_future}")
    if request.method == "POST":
        form = QuestionFourForm(request.POST, instance=question_four)
        if form.is_valid():
            form.save()
            return redirect("question_fours")

    form = QuestionFourForm(instance=question_four)
    return render(request, "form_template.html", {"form": form, "title": "Edit Question Four"})
