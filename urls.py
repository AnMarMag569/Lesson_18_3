
from django.contrib import admin
from django.urls import path
from task2.views import *
from task3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view/', func_view),
    path('class_view/', Class_view.as_view()),
    path('platform/', Platform_view.as_view()),
    path('games/', games_view),
    path('cart/', Cart_view.as_view()),
]
