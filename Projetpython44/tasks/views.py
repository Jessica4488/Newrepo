from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import escape
from django.utils.text import slugify
from django.template.loader import render_to_string

from tasks.models import Collection, Task


def index(request):
    context = {}

    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    context["collections"] = Collection.objects.order_by("slug")
    context["collection"] = collection
    context["tasks"] = collection.task_set.order_by("description")

    return render(request, 'tasks/index.html', context=context)


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))
    if not created:
        return HttpResponse("La collection existe déja.", status=409)

    return render(request, 'tasks/collection.html', context={"collection": collection})


def add_task(request):
    print(request.POST)
    collection = Collection.objects.get(slug=request.POST.get("collection"))
    description = escape(request.POST.get("task-description"))
    task = Task.objects.create(description=description, collection=collection)

    return render(request, 'tasks/task.html', context={"task": task})

def get_tasks(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.order_by("description")

    return render(request, 'tasks/tasks.html', context={"tasks": tasks})