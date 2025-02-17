import logging
from django.shortcuts import render, redirect
from ..models import InteractiveStyle
from ..forms import InteractiveStyleForm


def view_interactive_styles(request):
    queryset = InteractiveStyle.objects.all()
    interactive_styles = list(queryset.values())
    columns = [field.name for field in InteractiveStyle._meta.fields]
    logging.debug(f"there are {len(interactive_styles)} interactive styles, {interactive_styles}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": interactive_styles, "title": "Interactive Styles",
                   "edit_view": "edit_interactive_style","new_view":"create_interactive_style"})


def create_interactive_style(request):
    if request.method == "POST":
        form = InteractiveStyleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("interactive_styles")

    form = InteractiveStyleForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Interactive Style"})


def edit_interactive_style(request, pk: int):
    interactive_style = InteractiveStyle.objects.get(pk=pk)
    logging.debug(f"found interactive style : {interactive_style}, {interactive_style.description}")
    if request.method == "POST":
        form = InteractiveStyleForm(request.POST, instance=interactive_style)
        if form.is_valid():
            form.save()
            return redirect("interactive_styles")

    form = InteractiveStyleForm(instance=interactive_style)
    return render(request, "form_template.html", {"form": form, "title": "Edit Interactive Style"})
