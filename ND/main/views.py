from django.shortcuts import render
from typing import Any


def show_start(request: Any):
    return render(request, 'main/start.html')

def show_home(request: Any):
    return render(request, 'main/home.html')

def show_lorem(request: Any):
    return render(request, 'surprise/lorem.html')
