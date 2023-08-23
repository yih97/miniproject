from django.shortcuts import render
from .models import Coffee
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def category_page(request):
    if "cate" in request.GET:
        category = Coffee.objects.filter(coffee=request.GET["cate"])

    elif "br" in request.GET:
        category = Coffee.objects.filter(brand=request.GET["br"])

    else:
        category = Coffee.objects.all()

    return render(
        request,
        "coffee/coffee_list.html",
        {
            "coffee_list": category,
        }
    )



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



# def coffee_list(request):
#     items_per_page = 8  # 한 페이지당 커피 아이템 수
#     all_coffees = Coffee.objects.all()  # 모든 커피 아이템 가져오기
#
#     paginator = Paginator(all_coffees, items_per_page)  # 페이지네이션 설정
#     page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
#     page_coffees = paginator.get_page(page_number)  # 현재 페이지 커피 아이템 가져오기
#
#     return render(request, 'coffee_list.html', {'page_coffees': page_coffees})