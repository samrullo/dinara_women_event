from django import forms
from .models import (
    Language, Education, Responder, DifficultiesInJapan,
    SeminarTopics, InteractiveStyle, HowYouFoundUs,
    UseUzbekCommunityHelp, QuestionTwo, QuestionThree, QuestionFour
)


# 📌 Form for Responder
class ResponderForm(forms.ModelForm):
    class Meta:
        model = Responder
        fields = "__all__"
        widgets = {
            "languages": forms.CheckboxSelectMultiple(),
            "education": forms.Select(),
        }


# 📌 Form for Question Two
class QuestionTwoForm(forms.ModelForm):
    class Meta:
        model = QuestionTwo
        fields = "__all__"
        widgets = {
            "difficulties_in_japan": forms.CheckboxSelectMultiple(),
            "use_uzbek_community_help": forms.Select(),
        }


# 📌 Form for Question Three
class QuestionThreeForm(forms.ModelForm):
    class Meta:
        model = QuestionThree
        fields = "__all__"
        widgets = {
            "seminar_topic": forms.CheckboxSelectMultiple(),
            "interactive_style": forms.CheckboxSelectMultiple(),
        }


# 📌 Form for Question Four
class QuestionFourForm(forms.ModelForm):
    class Meta:
        model = QuestionFour
        fields = "__all__"
        widgets = {
            "howyoufoundus": forms.CheckboxSelectMultiple(),
        }


# 📌 Form for Language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"


# 📌 Form for Education
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"


# 📌 Form for Difficulties in Japan
class DifficultiesInJapanForm(forms.ModelForm):
    class Meta:
        model = DifficultiesInJapan
        fields = "__all__"


# 📌 Form for Seminar Topics
class SeminarTopicsForm(forms.ModelForm):
    class Meta:
        model = SeminarTopics
        fields = "__all__"


# 📌 Form for Interactive Style
class InteractiveStyleForm(forms.ModelForm):
    class Meta:
        model = InteractiveStyle
        fields = "__all__"


# 📌 Form for How You Found Us
class HowYouFoundUsForm(forms.ModelForm):
    class Meta:
        model = HowYouFoundUs
        fields = "__all__"


# 📌 Form for Use Uzbek Community Help
class UseUzbekCommunityHelpForm(forms.ModelForm):
    class Meta:
        model = UseUzbekCommunityHelp
        fields = "__all__"
