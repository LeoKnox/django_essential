from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListview.as_view()),
    path('notes/<int:pk>', views.DetailView.as_view()),
]