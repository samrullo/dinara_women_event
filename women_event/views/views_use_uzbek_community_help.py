import logging
from django.shortcuts import render, redirect
from ..models import UseUzbekCommunityHelp
from ..forms import UseUzbekCommunityHelpForm


def view_use_uzbek_community_help(request):
    queryset = UseUzbekCommunityHelp.objects.all()
    use_uzbek_community_help = list(queryset.values())
    columns = [field.name for field in UseUzbekCommunityHelp._meta.fields]
    logging.debug(
        f"there are {len(use_uzbek_community_help)} use uzbek community help records, {use_uzbek_community_help}")
    return render(request, "data_table.html",
                  {"columns": columns, "data": use_uzbek_community_help, "title": "Use Uzbek Community Help",
                   "edit_view": "edit_use_uzbek_community_help", "new_view": "create_use_uzbek_community_help"})


def create_use_uzbek_community_help(request):
    if request.method == "POST":
        form = UseUzbekCommunityHelpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("use_uzbek_community_help")

    form = UseUzbekCommunityHelpForm()
    return render(request, "form_template.html", {"form": form, "title": "Create Use Uzbek Community Help"})


def edit_use_uzbek_community_help(request, pk: int):
    use_uzbek_community_help = UseUzbekCommunityHelp.objects.get(pk=pk)
    logging.debug(
        f"found use uzbek community help : {use_uzbek_community_help}, {use_uzbek_community_help.description}")
    if request.method == "POST":
        form = UseUzbekCommunityHelpForm(request.POST, instance=use_uzbek_community_help)
        if form.is_valid():
            form.save()
            return redirect("use_uzbek_community_help")

    form = UseUzbekCommunityHelpForm(instance=use_uzbek_community_help)
    return render(request, "form_template.html", {"form": form, "title": "Edit Use Uzbek Community Help"})
