from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import redirect

from .models import *

def index(request, survey_id=None, default_values=None):
    request.session.set_test_cookie()
    if not request.session.test_cookie_worked():
        return HttpResponse("You need cookies enabed to respond to the survey")
    if survey_id == None:
        survey = Survey.objects.first()
        survey_id = survey.id
    else:
        survey = Survey.objects.get(pk=survey_id)
    if str(survey_id) in request.session:
        return render(request, 'survey/thank_you.html')
    context = {'survey': survey, 'default_values': default_values}
    return render(request, 'survey/show_survey.html', context)


def submit(request, survey_id):
    if request.method == 'POST':
        # validate
        for field in request.POST.keys():
            if field == "csrfmiddlewaretoken": continue
            question = Question.objects.get(pk=int(field))
            answer = Option.objects.get(pk=int(request.POST.get(field)))
            if not answer.question.id == question.id: raise
            if not question.section.survey.id == int(survey_id): raise
        survey = Survey.objects.get(pk=int(survey_id))
        for section in survey.section_set.all():
            for question in section.question_set.all():
                if not str(question.id) in request.POST.keys():
                    return index(request, survey_id, request.POST)

        # submit
        participation = SurveyParticipation()
        participation.survey = survey
        participation.save()
        for field in request.POST.keys():
            if field == "csrfmiddlewaretoken": continue
            question = Question.objects.get(pk=int(field))
            answer = Option.objects.get(pk=int(request.POST.get(field)))
            question_answer = QuestionAnswer()
            question_answer.participation = participation
            question_answer.question = question
            question_answer.answer = answer
            question_answer.save()
        request.session[str(survey_id)] = True
        return redirect('/')
    return index(request, survey_id)

def clear(request):
    request.session.flush()
    return redirect(index)
