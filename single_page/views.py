from django.shortcuts import render
from coffee.models import Coffee

# Create your views here.
def landing(request):
    return render(request, "single_page/landing.html")

def category_page(request, pk):
    category = Coffee.objects.get(pk=pk)

    return render(
        request,
        "coffee/coffee_list.html",
        {
            "categories": Coffee.objects.all(),
            "category": category,
        }
    )