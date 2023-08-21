from django.shortcuts import render
from .models import Coffee
from django.views.generic import ListView, DetailView

# Create your views here.

# def category_page(request, pk):
#     category = CoffeeList.objects.get(pk=pk)
#
#     return render(
#         request,
#         "coffee/coffee_list.html",
#         {
#             "categories": CoffeeList.objects.all(),
#             "category": category,
#         }
#     )

class CoffeeList(ListView):
    model = Coffee

class CoffeeDetail(DetailView):
    model = Coffee