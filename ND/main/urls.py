from django.urls import path
from .views import *

urlpatterns = [
    path("", show_start, name="start"),
    path("home", show_home, name="home"),
    path('l/o/r/e/m/_/i/p/s/u/m', show_lorem, name='lorem')
]


