from django.shortcuts import render
from django.http import HttpResponse
from product.models import Prduct


# Create your views here.
def home(request):
    product=Prduct.objects.all()
    return render(request, "web\home.html", context={"product":product})
