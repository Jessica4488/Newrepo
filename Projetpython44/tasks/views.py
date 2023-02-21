from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape

from tasks.models import Collection


def index(request):
    context = {}
    context["collections"] = Collection.objects.order_by("name")

    return render(request, 'tasks/index.html', context=context)

# on créer la vue et l'import
def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    Collection.objects.get_or_create(name=collection_name)
    return redirect('home')