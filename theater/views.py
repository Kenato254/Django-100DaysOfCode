from datetime import timedelta
from django.db.models import Q, F, ExpressionWrapper, Value
from django.db.models.functions import Coalesce, NullIf
from django.db.models.fields import CharField, DateTimeField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from theater.models import DogModel, PersonModel

from .forms import SearchModelForm
def search_view(request):
    if request.method == "POST":
        form = SearchModelForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search_bar"]
            results = Q(
                Q(name__icontains=search) |
                Q(job__icontains=search)|
                Q(country__name__icontains=search) 
            )
            return render(request, "theater/searchResults.html", {
                "search_results":PersonModel.objects.filter(results), 
                "query":PersonModel.objects.filter(results).query
            })
    return render(request, "theater/search.html", {"form": SearchModelForm()})

def list_countries_view(request):
    can = PersonModel.objects.annotate(
        can_donate_on = ExpressionWrapper(
            F('last_donated') - timedelta(days=56), output_field=DateTimeField())
    )
    full_name_view(request)
    return render(request, "theater/index.html", {'can': can})

# Database functions
# Performance Importance
def full_name_view(request):
    full_nameAnno = PersonModel.objects.annotate_full_name().filter(full_name__icontains="n").values_list("full_name")
    # Annotate creating dynamic field
    marital = PersonModel.objects.annotate(
        # ExpressionWrapper wraps expressions when mixed types  
        status=ExpressionWrapper(
            # Coelesce gets non-null values in a list
            Coalesce(
                # Return a null value is argument1 equals arguement2 otherwise return arguement1
                NullIf("marital_status", Value(" ")), "gender"
        ), output_field=CharField())
    ).values_list("status")
    print(marital)

def dogs_view(request):
    dogs=DogModel.objects.all()
    return render(request, 'theater/dogs.html', {'dogs':dogs})

def dog_detail_view(request, dog_pk):
    dog = DogModel.objects.get(id=dog_pk)
    return render(request, 'theater/copies.html', {"dog":dog})

def dog_copy_view(request, dog_pk):
    """ Makes a copy of an object"""
    dog = DogModel.objects.get(id=dog_pk)
    dog.id = None
    dog._state.adding = True
    dog.name = f"Copy_of_{dog.name}" 
    dog.save()
    return HttpResponseRedirect(reverse('theater:dogs-view'))

def dog_delete_view(request, dog_pk):
    dog = DogModel.objects.get(id=dog_pk)
    dog.delete()
    return render(request, 'theater/delete.html')