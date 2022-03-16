from django.shortcuts import render
from django.http import Http404
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListview(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    
class DetailView(DetailView):
    model = Notes
    context_object_name = "note"