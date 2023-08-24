from django.shortcuts import render
from .models import Coffee
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def category_page(request):
    # 데이터 필터링 기준 변수 초기화
    data_src = ""
    data_filter = ""

    # "cate" 파라미터가 있는지 확인
    if "cate" in request.GET:
        # 카테고리에 따른 커피 필터링
        category = Coffee.objects.filter(coffee=request.GET["cate"])
        data_src = request.GET["cate"]
        data_filter = "cate"
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
        print(request.POST.get("data_filter"))
        if request.POST.get("data_filter") == "cate":
            data = Coffee.objects.filter(coffee=request.POST.get("data_src"))
        # 브랜드 정보를 전달하는 경우 여기에서 조건 설정:
        # 브랜드 필터링 데이터 받아오기
        else:
            data = Coffee.objects.all()

        # 정렬 기준
        check_list = request.POST.get('check_list')
        # 오름차순 | 내림차순 (asc, desc)
        search_mode = request.POST.get('search_mode')
        if search_mode:
            if search_mode == 'desc':
                aaa = data.order_by(f'-{check_list}')
            else:
                aaa = data.order_by(f'{check_list}')

        # 페이지네이션을 위한 설정
        page_number = request.GET.get('page')
        page_size = 10  # 페이지당 아이템 개수 설정

        paginator = Paginator(aaa, page_size)
        page_obj = paginator.get_page(page_number)

        context = {'coffee_list': page_obj}
        return render(request, "coffee/coffee_detail.html", context)
