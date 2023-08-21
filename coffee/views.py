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
        # 정렬 기준
        coffee_list = request.POST.get('check_list')
        # 오름차순|내림차순 선택(asc, desc)
        search_mode = request.POST.get('search_mode')
        if search_mode:
            if search_mode == 'desc':
               aaa = Coffee.objects.order_by(f'-{coffee_list}')
            else:
               aaa = Coffee.objects.order_by(f'{coffee_list}')
        context = {'coffee_list': aaa}
    return render(request, "coffee/coffee_detail.html", context)