from django.contrib import admin
from django.urls import path
import tasks.views as views

# on créer les routes récupérer de views.py sauf celles qui sont là par défaut home et admin
urlpatterns = [
    path('', views.index, name="home"),
    path('add-collection', views.add_collection, name="add-collection"),
    path('add-task/<int:collection_pk>/', views.add_task, name="add-task"),
    path('get-tasks/<int:collection_pk>/', views.get_tasks, name="get-tasks"),
    path('admin/', admin.site.urls),
]


