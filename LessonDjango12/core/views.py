from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from datetime import datetime

def home_view(request):
    return render(request, 'core/base.html')

def about_view(request):
    return render(request, 'core/about.html')

def filter_demo_view(request):
    context = {
        "user_name": "Андрей Петухов",
        "long_text": "Я ел сухарики.",
        "today": datetime.now(),
        "empty_var": "",
        "item_list": ["Python", "Django", "PostgreSQL", "Docker"],
        "price": 1500.50
    }
    return render(request, 'core/filters.html', context)