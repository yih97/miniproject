from django.shortcuts import render
from .models import Coffee
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def category_page(request):
    # "cate" 파라미터가 있는지 확인
    if "cate" in request.GET:
        # 카테고리에 따른 커피 필터링
        category = Coffee.objects.filter(coffee=request.GET["cate"])
        data_src = request.GET["cate"]
        data_filter = "cate"
        # cate를 무엇으로 받을 건지

    # "br" 파라미터가 있는지 확인
    elif "br" in request.GET:
        # 브랜드에 따른 커피 필터링
        category = Coffee.objects.filter(brand=request.GET["br"])
        data_src = request.GET["br"]
        data_filter = "br"



    else:
        # 모든 커피 데이터 가져오기
        category = Coffee.objects.all()
        data_src = "all"
        data_filter = "none"

    # 페이지네이션을 위한 변수 초기화
    page_number = request.GET.get('page')
    page_size = 10

    # 페이지네이션 객체 생성
    paginator = Paginator(category, page_size)
    page_obj = paginator.get_page(page_number)


    return render(
        request,
        "coffee/coffee_list.html",
        {
            "coffee_list": page_obj,
            "data_src": data_src,
            "data_filter": data_filter,
        }
    )

class CoffeeList(ListView):
    model = Coffee

# class CoffeeDetail(DetailView):
#     model = Coffee

def check_list(request):
    if request.method == "POST":
        data_filter = request.POST.get("data_filter")
        data_src = request.POST.get("data_src")
        check_list = request.POST.get("check_list")
        search_mode = request.POST.get("search_mode")
        page_number = 1

    else:
        data_filter = request.GET.get("data_filter")
        data_src = request.GET.get("data_src")
        check_list = request.GET.get("check_list")
        search_mode = request.GET.get("search_mode")
        page_number = request.GET.get("page")

    data = Coffee.objects.all()  # 기본적으로 모든 커피 데이터를 가져옴

    if data_filter == "cate":
        data = Coffee.objects.filter(coffee=data_src)

    elif data_filter == "br":
        data = Coffee.objects.filter(brand=data_src)

    if search_mode:
        sort_order = f"-{check_list}" \
            if search_mode == "desc" \
            else check_list
        data = data.order_by(sort_order)

    page_size = 10

    paginator = Paginator(data, page_size)
    page_obj = paginator.get_page(page_number)

    context = {"coffee_list": page_obj,
               "data_filter": data_filter,
               "data_src": data_src,
               "check_list": check_list,
               "Search_mode": search_mode}

    return render(
        request,
        "coffee/coffee_detail.html",context)