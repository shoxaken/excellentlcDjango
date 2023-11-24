from rest_framework import serializers
from myfiles.models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date')

class Student_rusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_rus
        fields = ('__all__')

class Student_ArabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_arab
        fields = ("__all__")
class Student_matemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_matem
        fields = ("__all__")

class Student_mentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_mental
        fields = ("__all__")
class FanlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = ("__all__")

class Student_KeldiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bor
        fields = ('__all__')



class Student_KeldiToqSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorToq
        fields = ('__all__')

class QarzdorlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qarzdorlar
        fields = ('__all__')

class Student_VipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vip
        fields = ('__all__')

class Student_Ketgan(serializers.ModelSerializer):
    class Meta:
        model = Student_ketgan
        fields = ('__all__')

class AllPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_people
        fields = ('__all__')

    #
    # class Meta:
    #     model = Student_arab
    #     fields = (
    #     'id', 'ism', 'familya', 'yosh', 'manzil', 'dars_soati', 'telefon', 'telefon2', 'darajasi', 'Oquv_tanigan',
    #     'qaysi_ustoz', 'date')
    # class Meta:
    #     model = Student_matem
    #     fields = (
    #     'id', 'ism', 'familya', 'yosh', 'manzil', 'dars_soati', 'telefon', 'telefon2', 'darajasi', 'Oquv_tanigan',
    #     'qaysi_ustoz', 'date')
    #
    # class Meta:
    #     model = Student_mental
    #     fields = (
    #         'id', 'ism', 'familya', 'yosh', 'manzil', 'dars_soati', 'telefon', 'telefon2', 'darajasi', 'Oquv_tanigan',
    #         'qaysi_ustoz', 'date')