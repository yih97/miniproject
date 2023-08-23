from django.shortcuts import render
from .models import Coffee
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def category_page(request):
    if "cate" in request.GET:   # url 에 ?cate=가 들어가는지 확인
        category = Coffee.objects.filter(coffee=request.GET["cate"])


    elif "br" in request.GET:
        category = Coffee.objects.filter(brand=request.GET["br"])

        #  filter: 행의 제한을 거는 것
        # 컬럼명이 coffee 값이 "cate"에 해당되는
        # "cate"는 변수명
        # category로 coffee에서 해당 데이터 가져오기
        data_src = request.GET["cate"]
        # 받아온 데이터를 data_src라는 변수로 받기
        data_filter = "cate"


    elif "br" in request.GET:
        category = Coffee.objects.filter(brand=request.GET["br"])



    else:
        category = Coffee.objects.all()
        data_src = "all"
        data_filter = "none"
    # 아닌 경우에는 coffee 데이터를 모두 끌어오기

    return render(
        request,
        "coffee/coffee_list.html",      # coffee_list로 보냄
        {
            "coffee_list": category,        # category는 coffee_list
            "data_src" : data_src,          # data_src는 data_src
            "data_filter" : data_filter,    # data_filter 는 data_filter로 받기
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
        # elif 브랜드 정보 넘겨주게 되면 여기서 조건설정:
        #     브랜드 필터링 데이터 받아오기
        else:
            data = Coffee.objects.all()

        # 정렬 기준
        check_list = request.POST.get('check_list')
        # 오름차순|내림차순 선택(asc, desc)
        search_mode = request.POST.get('search_mode')
        if search_mode:
            if search_mode == 'desc':
               aaa = data.order_by(f'-{check_list}')
            else:
               aaa = data.order_by(f'{check_list}')
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