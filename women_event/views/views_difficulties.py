import logging
from django.shortcuts import render, redirect
from ..models import DifficultiesInJapan
from ..forms import DifficultiesInJapanForm


def view_difficulties(request):
    queryset = DifficultiesInJapan.objects.all()
    difficulties = list(queryset.values())
    columns = [field.name for field in DifficultiesInJapan._meta.fields]
    logging.debug(f"there are {len(difficulties)} difficulties, {difficulties}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": difficulties, "title": "Difficulties", "edit_view": "edit_difficulty",
                   "new_view": "create_difficulty"})


def create_difficulty(request):
    if request.method == "POST":
        form = DifficultiesInJapanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("difficulties")

    form = DifficultiesInJapanForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Difficulty"})


def edit_difficulty(request, pk: int):
    difficulty = DifficultiesInJapan.objects.get(pk=pk)
    logging.debug(f"found difficulty : {difficulty}, {difficulty.description}")
    if request.method == "POST":
        form = DifficultiesInJapanForm(request.POST)
        if form.is_valid():
            difficulty.description = form.cleaned_data["description"]
            difficulty.save()
            return redirect("difficulties")

    form = DifficultiesInJapanForm(instance=difficulty)
    return render(request, "form_template.html", {"form": form, "title": "Edit Difficulty"})
