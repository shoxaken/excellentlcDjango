from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import permissions , generics
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView ,get_object_or_404
from myfiles.models import *
from myfiles.serializer import *
from myfiles.tolovSerializer import *
from  myfiles.tolov5_10Serializer import *
from  myfiles.tolov10_15Serializer import  *
from  myfiles.tolov20_25Serializer import *
from  myfiles.tolov25_30Serializer import  *
from myfiles.kunlar import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import JuftKunSerializer
from .models import Juft_kunlari

class JuftKunlariDetailView(APIView):
    def get(self, request, pk):
        juft_kunlari = get_object_or_404(Juft_kunlari, pk=pk)
        serializer = JuftKunSerializer(juft_kunlari)
        return Response(serializer.data)

class ToqKunlariDetailViewByName(APIView):
    def get(self, request, ism):
        toq_kunlari = get_object_or_404(Toq_kunlari, ism=ism)  # Assuming 'name' is a field in your model
        serializer = ToqKunSerializer(toq_kunlari)
        return Response(serializer.data)

def index(malumot):
    return render(malumot,'index.html')
# Create your views here.

class IndexClass(ListView):
    model = Student
    template_name = "index.html"


# class ApiListClass(ListAPIView):
#     permission_classes = (permissions.AllowAny,)  # new
#     queryset = Student_rus.objects.all()
#     serializer_class = Student_rusSerializer

class ApiListClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ApiListTolovClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer

class ApiListTolov5_10Class(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Tolov5_10.objects.all()
    serializer_class = Tolov5_10Serializer

class ApiListTolov5_10TypeClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = TolovQilganYokiQilmaganType_20_25.objects.all()
    serializer_class = Tolov5_10TypeSerializer

class ApiListTolov10_15Class(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Tolov10_15.objects.all()
    serializer_class = Tolov10_15Serializer

class ApiListTolov20_25Class(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Tolov20_25.objects.all()
    serializer_class = Tolov20_25Serializer

class ApiListTolov25_30Class(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Tolov25_30.objects.all()
    serializer_class = Tolov25_30Serializer


class ApiListkunlarjuftClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Juft_kunlari.objects.all()
    serializer_class = JuftKunSerializer

class ApiAllPeopleClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = All_people.objects.all()
    serializer_class = AllPeopleSerializer

class ApiListkunlarjuftUdatepClass(UpdateAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Juft_kunlari.objects.all()
    serializer_class = JuftKunSerializer

class ApiListkunlarjuftReadClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Juft_kunlari.objects.all()
    serializer_class = JuftKunSerializer

class ApiListkunlartoqClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Toq_kunlari.objects.all()
    serializer_class = ToqKunSerializer

class ApiStudent_KeldiSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Bor.objects.all()
    serializer_class = Student_KeldiSerializer

class ApiStudent_KeldiToqSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = BorToq.objects.all()
    serializer_class = Student_KeldiToqSerializer

class ApiQardorlarSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Qarzdorlar.objects.all()
    serializer_class = QarzdorlarSerializer

class FanlarSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Fanlar.objects.all()
    serializer_class = FanlarSerializer

class ApiStudent_KeldiAddSerializerClass(CreateAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Bor.objects
    serializer_class = Student_KeldiSerializer

class ApiStudent_KeldiToqAddSerializerClass(CreateAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = BorToq.objects
    serializer_class = Student_KeldiToqSerializer

class ApiStudent_KetganSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student_ketgan.objects.all()
    serializer_class = Student_Ketgan
class ApiStudent_VipSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Vip.objects.all()
    serializer_class = Student_VipSerializer

class ApiArabSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student_arab.objects.all()
    serializer_class = Student_ArabSerializer


class ApiRusSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student_rus.objects.all()
    serializer_class = Student_rusSerializer


class ApimatemSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student_matem.objects.all()
    serializer_class = Student_matemSerializer

class ApimentalSerializerClass(ListAPIView):
    permission_classes = (permissions.AllowAny,)  # new
    queryset = Student_mental.objects.all()
    serializer_class = Student_mentalSerializer