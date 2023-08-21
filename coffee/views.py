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

# class CoffeeDetail(DetailView):
#     model = Coffee

def check_list(request):
    if request.POST:
        coffee_list = request.POST.getlist('check_list')

    search_mode = request.POST.getlist('search_mode')
    if search_mode:
        if search_mode == '높은 순':
           aaa = coffee_list.objects.order_by('컬럼명')
        else:
           aaa = coffee_list.objects.order_by('컬렴명')
    context = {'coffee_list': aaa}
    return render(request, "coffee/coffee_detail.html", context)