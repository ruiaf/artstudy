from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Section(models.Model):
    survey = models.ForeignKey(Survey)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.survey.title + ": " + self.title

class Question(models.Model):
    section = models.ForeignKey(Section)
    text = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    multiple_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.section.survey.title + ": question #" + str(self.order)

class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200, null=True, blank=True)
    hoovertext = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.text

class SurveyParticipation(models.Model):
    survey = models.ForeignKey(Survey)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return "participant #%i" % self.id

class QuestionAnswer(models.Model):
    participation = models.ForeignKey(SurveyParticipation)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Option)

    def __str__(self):
        return str(self.answer)
