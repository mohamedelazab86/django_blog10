from django.shortcuts import render
from .models import Post

# Create your views here.

# ======================== create crud opertions  by class based views   ========      cbv        ====
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class List_Post(ListView):                     # conext in template   name of model _list       post_list   object_list
    model=Post                                 # template     name of model _ actions           post_list
class Detail_post(DetailView):                 # context  in template   name of model           post  or object
    model=Post                                 # template in                                    post            

class create_post(CreateView):
    model=Post
    fields='__all__'
    template_name='posts/create.html'
    success_url='/posts/'

class update_post(UpdateView):
    model=Post
    fields='__all__'
    template_name='posts/edit.html'
    success_url='/posts/'
class Delete_post(DeleteView):
    model=Post
    success_url='/posts/'
    template_name='posts/delete.html'

