from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def add(request):
    """

    :param request:
    :return:
    """
    context = {}
    context['id'] = 0
    return render(request, 'add.html', context)


def del_(request):
    return HttpResponse("Del")


def show(request):
    return HttpResponse("Show")


def homepage(request):

    return render_to_response('index.html')