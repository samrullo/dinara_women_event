import logging
from django.shortcuts import render, redirect
from ..models import HowYouFoundUs
from ..forms import HowYouFoundUsForm


def view_how_you_found_us(request):
    queryset = HowYouFoundUs.objects.all()
    how_you_found_us = list(queryset.values())
    columns = [field.name for field in HowYouFoundUs._meta.fields]
    logging.debug(f"there are {len(how_you_found_us)} how you found us records, {how_you_found_us}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": how_you_found_us, "title": "How You Found Us",
                   "edit_view": "edit_how_you_found_us", "new_view": "create_how_you_found_us"})


def create_how_you_found_us(request):
    if request.method == "POST":
        form = HowYouFoundUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("how_you_found_us")

    form = HowYouFoundUsForm()
    return render(request, "form_template.html", {"form": form, "title": "Create How You Found Us"})


def edit_how_you_found_us(request, pk: int):
    how_you_found_us = HowYouFoundUs.objects.get(pk=pk)
    logging.debug(f"found how you found us : {how_you_found_us}, {how_you_found_us.description}")
    if request.method == "POST":
        form = HowYouFoundUsForm(request.POST, instance=how_you_found_us)
        if form.is_valid():
            form.save()
            return redirect("how_you_found_us")

    form = HowYouFoundUsForm(instance=how_you_found_us)
    return render(request, "form_template.html", {"form": form, "title": "Edit How You Found Us"})
