from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('detail/', views.courses_detail, name='courses_detail'),
    path('lesson/', views.courses_leasson, name='courses_leasson'),
]