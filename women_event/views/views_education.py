import logging
from django.shortcuts import render, redirect
from ..models import Education
from ..forms import EducationForm

def view_educations(request):
    queryset = Education.objects.all()
    educations = list(queryset.values())
    columns = [field.name for field in Education._meta.fields]
    logging.debug(f"there are {len(educations)} educations, {educations}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": educations, "title": "Education", "edit_view": "edit_education","new_view":"create_education"})

def create_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("educations")

    form = EducationForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Education"})

def edit_education(request, pk: int):
    education = Education.objects.get(pk=pk)
    logging.debug(f"found education : {education}, {education.education}")
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education.education = form.cleaned_data["education"]
            education.save()
            return redirect("educations")

    form = EducationForm({"education": education.education})
    return render(request, "form_template.html", {"form": form, "title": "Edit Education"})
