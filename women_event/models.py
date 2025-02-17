from django.db import models


# ✅ Language Model
class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


# ✅ Education Model
class Education(models.Model):
    education = models.CharField(max_length=50)

    def __str__(self):
        return self.education


# ✅ Difficulties in Japan Model
class DifficultiesInJapan(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description


# ✅ Seminar Topics Model
class SeminarTopics(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description


# ✅ Interactive Style Model
class InteractiveStyle(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


# ✅ How You Found Us Model
class HowYouFoundUs(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


# ✅ Use Uzbek Community Help Model
class UseUzbekCommunityHelp(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


# ✅ Responder Model
class Responder(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    languages = models.ManyToManyField(Language, blank=True)
    years_in_japan = models.IntegerField()
    living_city = models.CharField(max_length=50)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True)
    education_details = models.CharField(max_length=100, null=True)
    does_work = models.BooleanField(default=False)
    workplace = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} ({self.age} years old) - {self.living_city}"


# ✅ Question Two Model
class QuestionTwo(models.Model):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE)
    difficulties_in_japan = models.ManyToManyField(DifficultiesInJapan)
    difficulties_in_japan_other = models.CharField(max_length=1000, null=True)
    your_priority_problem = models.CharField(max_length=1000, null=True)
    use_uzbek_community_help = models.ForeignKey(UseUzbekCommunityHelp, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Q2 - {self.responder.name}: {self.your_priority_problem[:50]}..."


# ✅ Question Three Model
class QuestionThree(models.Model):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE)
    seminar_topic = models.ManyToManyField(SeminarTopics)
    seminar_topic_other = models.CharField(max_length=100, null=True)
    interactive_style = models.ManyToManyField(InteractiveStyle)
    comments = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"Q3 - {self.responder.name}: {self.seminar_topic_other}"


# ✅ Question Four Model
class QuestionFour(models.Model):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE)
    improvements_for_future = models.TextField(null=True)
    howyoufoundus = models.ManyToManyField(HowYouFoundUs)
    howyoufoundus_other = models.CharField(max_length=100)

    def __str__(self):
        return f"Q4 - {self.responder.name}: {self.howyoufoundus_other}"
