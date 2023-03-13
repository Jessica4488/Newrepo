from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape

from tasks.models import Collection


def index(request):
    context = {}

    collection = Collection.get_default_collection()
    context["collections"] = Collection.objects.order_by("slug")

    return render(request, 'tasks/index.html', context=context)

# on créer la vue et l'import
def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déja.", status=409)

    return HttpResponse(f'<h2>{collection_name}</h2>')


def add_task(request):
    collection = Collection.get_default_collection()

    description = request.POST.
    Task.objects.create(description=request.POST.get(""))


    return HttpResponse("")