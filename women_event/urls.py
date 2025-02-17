from django.urls import path
from .views import (home,
                    views_language, views_education, views_responder,
                    views_difficulties, views_question_two, views_question_three,
                    views_question_four, views_seminar_topics, views_interactive_style,
                    views_how_you_found_us, views_use_uzbek_community_help,
                    view_difficulties_in_japan_stats, view_does_work_stats, view_seminars_stats,
                    view_interactive_styles_stats, view_howyoufoundus_stats,
                    view_language_stats, view_education_stats)

urlpatterns = [
    path("", home, name="home"),
    # ✅ Language URLs
    path("languages/", views_language.view_languages, name="languages"),
    path("languages/create/", views_language.create_language, name="create_language"),
    path("languages/edit/<int:pk>/", views_language.edit_language, name="edit_language"),

    # ✅ Education URLs
    path("educations/", views_education.view_educations, name="educations"),
    path("educations/create/", views_education.create_education, name="create_education"),
    path("educations/edit/<int:pk>/", views_education.edit_education, name="edit_education"),

    # ✅ Responder URLs
    path("responders/", views_responder.view_responders, name="responders"),
    path("responders/create/", views_responder.create_responder, name="create_responder"),
    path("responders/edit/<int:pk>/", views_responder.edit_responder, name="edit_responder"),

    # ✅ Difficulties in Japan URLs
    path("difficulties/", views_difficulties.view_difficulties, name="difficulties"),
    path("difficulties/create/", views_difficulties.create_difficulty, name="create_difficulty"),
    path("difficulties/edit/<int:pk>/", views_difficulties.edit_difficulty, name="edit_difficulty"),

    # ✅ Question Two URLs
    path("question_twos/", views_question_two.view_question_twos, name="question_twos"),
    path("question_twos/create/", views_question_two.create_question_two, name="create_question_two"),
    path("question_twos/edit/<int:pk>/", views_question_two.edit_question_two, name="edit_question_two"),

    # ✅ Question Three URLs
    path("question_threes/", views_question_three.view_question_threes, name="question_threes"),
    path("question_threes/create/", views_question_three.create_question_three, name="create_question_three"),
    path("question_threes/edit/<int:pk>/", views_question_three.edit_question_three, name="edit_question_three"),

    # ✅ Question Four URLs
    path("question_fours/", views_question_four.view_question_fours, name="question_fours"),
    path("question_fours/create/", views_question_four.create_question_four, name="create_question_four"),
    path("question_fours/edit/<int:pk>/", views_question_four.edit_question_four, name="edit_question_four"),

    # ✅ Seminar Topics URLs
    path("seminar_topics/", views_seminar_topics.view_seminar_topics, name="seminar_topics"),
    path("seminar_topics/create/", views_seminar_topics.create_seminar_topic, name="create_seminar_topic"),
    path("seminar_topics/edit/<int:pk>/", views_seminar_topics.edit_seminar_topic, name="edit_seminar_topic"),

    # ✅ Interactive Style URLs
    path("interactive_styles/", views_interactive_style.view_interactive_styles, name="interactive_styles"),
    path("interactive_styles/create/", views_interactive_style.create_interactive_style,
         name="create_interactive_style"),
    path("interactive_styles/edit/<int:pk>/", views_interactive_style.edit_interactive_style,
         name="edit_interactive_style"),

    # ✅ How You Found Us URLs
    path("how_you_found_us/", views_how_you_found_us.view_how_you_found_us, name="how_you_found_us"),
    path("how_you_found_us/create/", views_how_you_found_us.create_how_you_found_us, name="create_how_you_found_us"),
    path("how_you_found_us/edit/<int:pk>/", views_how_you_found_us.edit_how_you_found_us, name="edit_how_you_found_us"),

    # ✅ Use Uzbek Community Help URLs
    path("use_uzbek_community_help/", views_use_uzbek_community_help.view_use_uzbek_community_help,
         name="use_uzbek_community_help"),
    path("use_uzbek_community_help/create/", views_use_uzbek_community_help.create_use_uzbek_community_help,
         name="create_use_uzbek_community_help"),
    path("use_uzbek_community_help/edit/<int:pk>/", views_use_uzbek_community_help.edit_use_uzbek_community_help,
         name="edit_use_uzbek_community_help"),
    path("difficulties_in_japan/", view_difficulties_in_japan_stats, name="difficulties_in_japan"),
    path("does_work_stats/", view_does_work_stats, name="does_work_stats"),
    path("seminar_topics_stats/", view_seminars_stats, name="seminar_topics_stats"),
    path("interactive_stye_stats/", view_interactive_styles_stats, name="interactive_stye_stats"),
    path("howyoufoundus_stats/", view_howyoufoundus_stats, name="howyoufoundus_stats"),
    path("languages_stats/", view_language_stats, name="languages_stats"),
    path("education_stats/", view_education_stats, name="education_stats")
]
