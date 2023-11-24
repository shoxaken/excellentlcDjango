from rest_framework import serializers
from myfiles.models import *



class JuftKunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juft_kunlari
        fields = ('__all__')


class ToqKunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toq_kunlari
        fields = ('__all__')