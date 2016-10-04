from django.contrib import admin

from .models import *

class OptionInline(admin.StackedInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    model = Question 
    inlines = [
        OptionInline,
    ]

class QuestionInline(admin.StackedInline):
    model = Question

class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [
        QuestionInline,
    ]

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0

class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    inlines = [
        SectionInline,
    ]

class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer
    extra = 0

class SurveyParticipationAdmin(admin.ModelAdmin):
    model = SurveyParticipation
    inlines = [
        QuestionAnswerInline,
    ]

# Register your models here.
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(SurveyParticipation, SurveyParticipationAdmin)
