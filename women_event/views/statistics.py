import logging
import json
from django.shortcuts import render
from ..models import DifficultiesInJapan, Responder, SeminarTopics, InteractiveStyle, HowYouFoundUs, Language, Education


def view_difficulties_in_japan_stats(request):
    """
    View function to display statistics for difficulties faced in Japan using the generic stats template.
    """
    difficulties = DifficultiesInJapan.objects.all()
    difficulties_count = {difficulty.description: difficulty.questiontwo_set.count() for difficulty in difficulties}

    # Sort data in descending order
    difficulties_count = dict(sorted(difficulties_count.items(), key=lambda item: item[1], reverse=True))

    logging.debug(f"Difficulties in Japan: {difficulties_count}")

    return render(request, "stats/count_stats_template.html", {
        "title": "Yaponiyada qiyinchiliklar",
        "column_name": "Qiyinchilik",
        "stats_data": difficulties_count,  # ✅ Raw dictionary for the table
        "stats_data_json": json.dumps(difficulties_count)  # ✅ JSON for D3.js
    })


def view_does_work_stats(request):
    """
    View function to display statistics for employed vs. unemployed responders using the generic stats template.
    """
    responders = Responder.objects.all()
    who_work = sum(1 for responder in responders if responder.does_work)
    who_work_not = sum(1 for responder in responders if not responder.does_work)

    logging.info(f"{who_work} who work, {who_work_not} who do not work")

    data = {"Ha": who_work, "Yo'q": who_work_not}

    return render(request, "stats/count_stats_template.html", {
        "title": "Ishlayman?",
        "column_name": "Ishlayman?",
        "stats_data": data,  # ✅ Raw dictionary for the table
        "stats_data_json": json.dumps(data)  # ✅ JSON for D3.js
    })


def view_seminars_stats(request):
    """
    View function to display seminar topic statistics using the generic stats template.
    """
    seminar_topics = SeminarTopics.objects.all()
    st_count = {record.description: record.questionthree_set.count() for record in seminar_topics}

    # Sort data in descending order
    st_count = dict(sorted(st_count.items(), key=lambda item: item[1], reverse=True))

    return render(request, "stats/count_stats_template.html", {
        "title": "Seminar mavzulari statistikasi",
        "column_name": "Seminar mavzusi",
        "stats_data": st_count,  # ✅ Pass raw dictionary for table rendering
        "stats_data_json": json.dumps(st_count)  # ✅ Convert to JSON only for D3.js
    })


def view_interactive_styles_stats(request):
    interactive_styles = InteractiveStyle.objects.all()
    data_dict = {record.description: record.questionthree_set.count() for record in interactive_styles}
    data_dict = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))

    return render(request, "stats/count_stats_template.html",
                  {"title": "Qaysi interaktiv shakl qulayroq?", "column_name": "Interaktiv shakl",
                   "stats_data": data_dict,
                   "stats_data_json": json.dumps(data_dict)})


def view_howyoufoundus_stats(request):
    records = HowYouFoundUs.objects.all()
    data_dict = {record.description: record.questionfour_set.count() for record in records}
    data_dict = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))

    return render(request, "stats/count_stats_template.html",
                  {"title": "Bizni qanday topdingiz?", "column_name": "Xabar topish usuli",
                   "stats_data": data_dict,
                   "stats_data_json": json.dumps(data_dict)})


def view_language_stats(request):
    records = Language.objects.all()
    data_dict = {record.language: record.responder_set.count() for record in records}
    data_dict = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))

    return render(request, "stats/count_stats_template.html",
                  {"title": "Qaysi tillarni bilasiz?", "column_name": "Til",
                   "stats_data": data_dict,
                   "stats_data_json": json.dumps(data_dict)})


def view_education_stats(request):
    records = Education.objects.all()
    data_dict = {record.education: record.responder_set.count() for record in records}
    data_dict = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
    return render(request, "stats/count_stats_template.html",
                  {"title": "Ta'lim statistikasi", "column_name": "Ta'lim darajasi",
                   "stats_data": data_dict,
                   "stats_data_json": json.dumps(data_dict)})
