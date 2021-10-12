from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from livros.models import Livros

class LivroList(ListView):
    model = Livros
    queryset = Livros.objects.all()

class LivroCreate(CreateView):
    model = Livros
    fields = '__all__'
    success_url = reverse_lazy('livros:list')

class LivroUpdate(UpdateView):
    model = Livros
    fields = '__all__'
    success_url = reverse_lazy('livros:list')

class LivroDetail(DetailView):
    queryset = Livros.objects.all()

class LivroDelete(DeleteView):
    queryset = Livros.objects.all()
    success_url = reverse_lazy('livros:list')