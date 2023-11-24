"""
URL configuration for djangofiles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myfiles.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('rest_framework.urls')), # new
    path('', index,name='index'),
    path('sdu/', index,name='IndexClass'),
    path('api/', ApiListClass.as_view()),
    path('tolovapi/', ApiListTolovClass.as_view()),
    path('tolov5_10api/', ApiListTolov5_10Class.as_view()),
    path('tolov10_15api/', ApiListTolov10_15Class.as_view()),
    path('tolov20_25api/', ApiListTolov20_25Class.as_view()),
    path('tolov25_30api/', ApiListTolov25_30Class.as_view()),
    path('juftapi/', ApiListkunlarjuftClass.as_view()),
    path('juftapi/<int:pk>/', JuftKunlariDetailView.as_view()),
    path('update/<pk>/', ApiListkunlarjuftUdatepClass.as_view()),
    path('toqapi/', ApiListkunlartoqClass.as_view()),
    path('allpeople/', ApiAllPeopleClass.as_view()),
    path('tovqilganType/', ApiListTolov5_10TypeClass.as_view()),
    path('toqapi/<str:ism>/', ToqKunlariDetailViewByName.as_view(), name='toqkunlari-detail-by-ism'),
    path('keldi/', ApiStudent_KeldiSerializerClass.as_view()),
    path('keldiToq/', ApiStudent_KeldiToqSerializerClass.as_view()),
    path('keldiadd/', ApiStudent_KeldiAddSerializerClass.as_view()),
    path('keldiToqadd/', ApiStudent_KeldiToqAddSerializerClass.as_view()),
    path('ketgan/', ApiStudent_KetganSerializerClass.as_view()),
    path('Vip/', ApiStudent_VipSerializerClass.as_view()),
    path('qarzdorlar/', ApiQardorlarSerializerClass.as_view()),
    path('StudentArab/', ApiArabSerializerClass.as_view()),
    path('Studentrus/', ApiRusSerializerClass.as_view()),
    path('Studentmatem/', ApimatemSerializerClass.as_view()),
    path('Studentmental/', ApimentalSerializerClass.as_view()),
    path('Fanlar/', FanlarSerializerClass.as_view()),



]
