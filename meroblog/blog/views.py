from django.shortcuts import render
from .models import MainMenu, Blog
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contact_list = MainMenu.objects.all()
    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    menuData = paginator.get_page(page)
    data = {
        'allData': menuData
    }

    return render(request,'pages/index.html', data)

def category(request,slug):

    data = {
        'menuDetails': MainMenu.objects.get(slug=slug)
    }
    return render(request, 'pages/blog.html', data)

def blog(request):
    data = {
        'menuDetails': Blog.objects.all
    }
    return render(request, 'pages/blog.html', data)
