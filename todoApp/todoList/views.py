from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task


def index(request):
    return render(request, 'base.html')


def submit(request):
    obj = Task()
    obj.task_title = request.GET['title']
    obj.task_text = request.GET['description']
    obj.task_status = request.GET['status']
    obj.save()
    mydict = {
        "alltodos": Task.objects.order_by('-id')
    }
    return render(request, 'list.html', context=mydict)


def list(request):
    mydict = {
        "alltodos": Task.objects.order_by('-id')
    }
    return render(request, 'list.html', context=mydict)


def delete(request, id):
    obj = Task.objects.get(id=id)
    obj.delete()
    mydict = {
        "alltodos": Task.objects.order_by('-id')
    }
    return render(request, 'list.html', context=mydict)


def edit(request, id):
    obj = Task.objects.get(id=id)
    mydict = {
        "id" : id,
        "title": obj.task_title,
        "description": obj.task_text,
        "status": obj.task_status
    }
    return render(request, 'edit.html', context=mydict)


def update(request, id):
    obj = Task.objects.get(id=id)
    obj.task_title = request.GET['title']
    obj.task_text = request.GET['description']
    obj.task_status = request.GET['status']
    obj.save()
    mydict = {
        "alltodos": Task.objects.order_by('-id')
    }
    return render(request, 'list.html', context=mydict)
