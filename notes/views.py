from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListview(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()
    
class DetailView(DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/admin"