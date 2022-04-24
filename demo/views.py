from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.template import loader
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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


# def redirect(request):
#     return HttpResponseRedirect(reverse('demo:url_standard_fix'))


# Class base views
class Class_Base_View(View):

    def get(self, request):
        return HttpResponse("cbv for get method")

    def post(self, request):
        return HttpResponse("CBV for post method")

# render templates


def get_model(request, pk):
    question = Question.objects.get(pk=pk)
    questions = Question.objects.all()
    context = {
        'question': question,
        'questions': questions,
    }
    return render(request, 'detail.html', context)


@login_required(login_url='demo:login')
def index(request):
    return render(request, 'index.html')
    # cookie method
    # data = request.POST
    # username = data.get('username')
    # password = data.get('password')
    # keep = data.get('keep')
    # if username == 'shane' and password == '123':
    #     response = HttpResponse()
    #     context = {
    #         'username': username,
    #         'password': password,
    #     }
    #     template = loader.get_template('index.html')
    #     response.content = template.render(context, request)
    #     if keep == 'keep':
    #         response.set_cookie('username', username, max_age=3 * 24 * 3600)
    #         response.set_signed_cookie(
    #             'password', password, salt='abc', max_age=3 * 24 * 3600)
    #     else:
    #         response.delete_cookie('username')
    #         response.delete_cookie('password')
    #     return response
    # else:
    #     return HttpResponseRedirect(reverse('demo:login'))


def login(request):
    if request.method == 'GET':
        error_msg = request.session.get('error_msg')
        request.session['error_msg'] = None
        return render(request, 'login.html', {'error_msg': error_msg})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('demo:index')
        else:
            request.session['error_msg'] = 'wrong username or password!'
            return redirect('demo:login')
    # username = request.COOKIES.get('username')
    # password = request.get_signed_cookie('password', None, salt='abc')
    # if username and password:
    #     return render(request, 'login.html', {'username': username, 'password': password})
    # return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
