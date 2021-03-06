from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListview.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.DetailView.as_view(), name="notes.detail"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('ntes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
]