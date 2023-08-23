from django.shortcuts import render
from coffee.models import Coffee

# Create your views here.
def landing(request):
    category = Coffee.objects.all().values("coffee").distinct()
    return render(request, "single_page/landing.html", {"category" : category})

# def category_page(request):
#
#
#     return render(
#         request,
#         "coffee/coffee_list.html",
#         {
#             "categories": Coffee.objects.all(),
#             "category": category,
#         }
#     )