from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Categories,Items

# Create your views here.

def index(request,*args, **kwargs):
    return render(request,"homepage.html")

def get_categories(request):
    post = Categories.objects.all()
    return render(request,"categories.html",context={"posts":post})

def get_items(request,id):
    categor = Categories.objects.get(id=id)
    post = Items.objects.filter(category = categor)
    # return HttpResponse("got item id {}".format(data))
    return render(request,"items.html",context={"posts":post})

def get_item_view(request,id):
    print("request",id)
    post = Items.objects.get(id=id)
    return render(request,"item_view.html",context={"posts":post})
