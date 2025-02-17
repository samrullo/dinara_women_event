import logging
from django.shortcuts import render, redirect
from ..models import Responder
from ..forms import ResponderForm

import logging
from django.shortcuts import render, redirect
from ..models import Responder
from django.conf import settings
import json


def view_responders(request):
    col_map_file = settings.BASE_DIR / "data" / "responders_en_to_uz.json"
    col_mappings = json.loads(col_map_file.read_text(encoding="utf-8"))
    responders = Responder.objects.all().select_related("education").prefetch_related("languages")

    columns = ["id", "name", "age", "years_in_japan", "living_city", "education","education_details", "does_work", "workplace"]
    columns_translated = [col_mappings[col] if col in col_mappings else col for col in columns]

    logging.debug(f"there are {len(responders)} responders, {responders}")

    return render(request, "responders/data_table.html", {
        "columns": columns_translated,
        "data": responders,
        "title": "1-bo'lim. Shaxsiy ma'lumotlar",
        "edit_view": "edit_responder",
        "new_view": "create_responder"
    })


def create_responder(request):
    if request.method == "POST":
        form = ResponderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("responders")

    form = ResponderForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Responder"})


def edit_responder(request, pk: int):
    responder = Responder.objects.get(pk=pk)
    logging.debug(f"found responder : {responder}, {responder.name}")
    if request.method == "POST":
        form = ResponderForm(request.POST)
        if form.is_valid():
            for field in form.cleaned_data:
                setattr(responder, field, form.cleaned_data[field])
            responder.save()
            return redirect("responders")

    form = ResponderForm(instance=responder)
    return render(request, "form_template.html", {"form": form, "title": "Edit Responder"})
