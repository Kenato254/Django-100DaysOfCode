from django.contrib.auth import views
from django.http.response import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


from codeApp.models import Author
from codeApp.forms import Author, MessageMeForm

class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    
    def form_invalid(self, form):
        """ Form Error handler with Json Response"""
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse (
                {
                    'pk':self.object.pk
                }
            )

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    template_name = 'jSon/author_create.html'
    

class AuthorListView(ListView):
    template_name = 'jSon/author_list.html'
    context_object_name = 'authors'
    paginate_by = 4
    queryset = Author.objects.all()


# Mixing DetailView with FormView
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'jSon/author_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageMeForm()
        return context
    

class AuthorMessageMeView(SingleObjectMixin, FormView):
    model = Author
    form_class = MessageMeForm
    success_url = reverse_lazy('jSon:authors-list')

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden("Request not allowed. Login first to proceed.")
        self.object = self.get_object()
        self.get_context_data()
        return super().post(request, *args, **kwargs)
    
class AuthorView(View):
    def get(self, request, *args, **kwargs):
        view = AuthorDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = AuthorMessageMeView.as_view()
        return view(request, *args, **kwargs)