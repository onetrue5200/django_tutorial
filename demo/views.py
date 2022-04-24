from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from demo.models import *


def url_standard_fix(request):
    return HttpResponse("url standard fix!")


def url_standard_number(request, number=-1):
    return HttpResponse(f"url standard number: {number}")


def url_standard_uuid(request, uuid):
    return HttpResponse(f"url standard uuid: {uuid}")


def url_standard_str(request, str):
    return HttpResponse(f"aurl standard str: {str}")


def url_standard_slug(request, slug):
    return HttpResponse(f"url standard slug: {slug}")


def url_standard_path(request, path):
    return HttpResponse(f"url standard path: {path}")


def url_custom_year(request, year):
    return HttpResponse(f"url custom year: {year}")


def page_not_found(request, exception):
    return HttpResponse("appear 404")


def redirect(request):
    return HttpResponseRedirect(reverse('demo:url_standard_fix'))


# Class base views
class Class_Base_View(View):

    def get(self, request):
        return HttpResponse("cbv for get method")

    def post(self, request):
        return HttpResponse("CBV for post method")

# render templates


def index(request):
    context = {
        'key': 'value',
    }
    return render(request, "index.html", context)


def get_model(request, pk):
    question = Question.objects.get(pk=pk)
    questions = Question.objects.all()
    context = {
        'question': question,
        'questions': questions,
    }
    return render(request, 'detail.html', context)
