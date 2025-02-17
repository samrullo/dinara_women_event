import logging
from django.shortcuts import render, redirect
from ..models import SeminarTopics
from ..forms import SeminarTopicsForm

def view_seminar_topics(request):
    queryset = SeminarTopics.objects.all()
    seminar_topics = list(queryset.values())
    columns = [field.name for field in SeminarTopics._meta.fields]
    logging.debug(f"there are {len(seminar_topics)} seminar topics, {seminar_topics}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": seminar_topics, "title": "Seminar Topics", "edit_view": "edit_seminar_topic","new_view":"create_seminar_topic"})

def create_seminar_topic(request):
    if request.method == "POST":
        form = SeminarTopicsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("seminar_topics")

    form = SeminarTopicsForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Seminar Topic"})

def edit_seminar_topic(request, pk: int):
    seminar_topic = SeminarTopics.objects.get(pk=pk)
    logging.debug(f"found seminar topic : {seminar_topic}, {seminar_topic.description}")
    if request.method == "POST":
        form = SeminarTopicsForm(request.POST, instance=seminar_topic)
        if form.is_valid():
            form.save()
            return redirect("seminar_topics")

    form = SeminarTopicsForm(instance=seminar_topic)
    return render(request, "form_template.html", {"form": form, "title": "Edit Seminar Topic"})
