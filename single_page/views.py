from django.shortcuts import render
from coffee.models import Coffee


def landing(request):
    category = Coffee.objects.all().values("coffee").distinct()
    return render(request, "single_page/landing.html", {"category" : category})

