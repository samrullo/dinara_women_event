import logging
from django.shortcuts import render, redirect
from ..models import Language
from ..forms import LanguageForm


def view_languages(request):
    queryset = Language.objects.all()
    languages = list(queryset.values())
    columns = [field.name for field in Language._meta.fields]
    logging.debug(f"there are {len(languages)} languages, {languages}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": languages, "title": "Languages", "edit_view": "edit_language",
                   "new_view": "create_language"})


def create_language(request):
    if request.method == "POST":
        form = LanguageForm(request.POST, request.FILES)  # Handles file uploads too
        if form.is_valid():
            form.save()
            return redirect("languages")  # Redirect after successful submission

    form = LanguageForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Language"})


def edit_language(request, pk: int):
    language = Language.objects.get(pk=pk)
    logging.debug(f"found language : {language}, {language.language}")
    if request.method == "POST":
        form = LanguageForm(request.POST, request.FILES)  # Handles file uploads too
        if form.is_valid():
            language.language = form.cleaned_data["language"]
            language.save()
            return redirect("languages")  # Redirect after successful submission
    form = LanguageForm({"language": language.language})
    return render(request, "form_template.html", {"form": form, "title": "Edit Language"})
