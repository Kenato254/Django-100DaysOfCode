from typing import List
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views import View
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import ListView

from codeApp.mixins import JsonTemplateView
from .models import Author, BookModel, User
from codeApp.forms import BookModelForm, ContactForm

 # NOT SO DRY
class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        resp = super().get(request, *args, **kwargs)
        if not request.session.get('secrets') and not request.session.get('visits'):
            request.session['secrets'] = '|4?:jjrK&Q\'/0lY5FlQn=1St_M,tu87#wn}7Yf4YYe(Hh"K+gy'
            request.session["visits"] = 1
        session = request.session.get('visit')
        print(request.META)
        return resp


# Using Mixins
class BookListView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'codeApp/list_books.html'

    def get(self, request):
        return render(request, self.template_name, self.get_queryset())

    def get_queryset(self):
        user = self.request.user
        # print(f'{user.userprofile} is an instance of {User} {isinstance(user, User)}')
        queryset = {
            "book_list" : BookModel.objects.filter(user=user),
        }
        return queryset  

    # Method not working as intended.
    # def head(self, *args, **kwargs):
    #     book_list = self.get_queryset().latest('pub_date')
    #     print(book_list)
    #     response = HttpResponse(
    #         headers={'last_modified':book_list.pub_date.ctime()
    #     })
    #     return response

# EVERY instance of this view is decorated 
@method_decorator(login_required, name='dispatch')
class BookAddView(ModelFormMixin, View):
    form_class = BookModelForm
    template_name = "codeApp/add_book.html"

    def get(self, request):
        form = self.form_class()
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            #! Sets cookie
            signed_object = signer.sign_object({'Test': 'Cookie'})
            request.set_cookie('object', signed_object, max_age=300)
            
            #! Sets Session
            num_of_visits = request.session.get('num_of_visits', 0) + 1
            request.session['num_of_visits'] = num_of_visits
            if num_of_visits > 4: del(request.session['num_of_visits'])
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            pub_date = form.cleaned_data["pub_date"]
            book = BookModel.objects.create(
                name=name,
                pub_date=pub_date,
                user = user,
                userprofile = user.userprofile
            )
            book.save()
            return HttpResponseRedirect("/book-list/")
        return render(request, self.template_name, {'form':form})

class BookDetailView(ContextMixin, View):
    # model =BookModel
    template_name = 'codeApp/view_book.html'

    def get(self, request, *args, **kwargs):
        context = {'book':self.get_queryset(), 'total_books': self.get_context_data()['adds_extra_context']}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adds_extra_context'] = BookModel.objects.all().count()
        return context

    def get_queryset(self):
        query = BookModel.objects.get(id=self.kwargs['pk'])
        return query
    

# Decorated in the URLconf
class BookUpdateView(View):
    template_name = 'codeApp/update_book.html'
    form_class = BookModelForm

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name,{
                'form': self.form_class(instance=self.get_queryset()), 'book':self.get_queryset()
            }
        )
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            book = self.get_queryset()
            book.name = form.cleaned_data['name']
            book.pub_date = form.cleaned_data['pub_date']
            book.save()
            return redirect('codeApp:view-book', pk=self.kwargs['pk'])

        return self.get(request)

    def get_queryset(self):
        query = BookModel.objects.get(id=self.kwargs['pk'])
        return query
    
# View method dispatch decorated
class BookDeleteView(View):
    template_name = 'codeApp/remove_book.html'

    # To decorate every instance of a CBV apply decorator to dispatch()
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"book":self.get_queryset()})

    def post(self, request, *args, **kwargs):
        book = self.get_queryset()
        book.delete()
        return redirect('/book-list/')

    def get_queryset(self):
        queryset = BookModel.objects.get(id=self.kwargs['pk'])
        return queryset

class ContactFormView(generic.FormView):
    template_name = 'codeApp/contact_form.html'
    form_class = ContactForm
    # success_url = reverse_lazy('codeApp:view-books')

    def form_valid(self, form): 
        send_mail(
            subject = form.cleaned_data['name'],   
            message = form.cleaned_data['body'],
            from_email = form.cleaned_data['email'],
            recipient_list = ['test@gmail.com'],
        )
        return super().form_valid(form)
            

    def get_success_url(self):
        return reverse('codeApp:view-books')

class JsonTemplateView(JsonTemplateView, View):
    model = BookModel
    template_name = 'codeApp/json_date.html'

    
class BokListView(SingleObjectMixin, ListView):
    paginator_by = 2
    templates_name = 'codeApp/list_books_pag.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=BookModel.objects.all())
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['book_list'] = self.object
        return context
    
    def get_queryset(self):
        return self.object.author_set.all()
