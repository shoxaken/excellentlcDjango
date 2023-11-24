from rest_framework import serializers
from myfiles.models import *


class TolovQilganYokiQilmaganTypeSerializer15_20(serializers.ModelSerializer):
    class Meta:
        model = TolovQilganYokiQilmaganType
        fields = '__all__'

class TolovSerializer(serializers.ModelSerializer):
    tolov_filter = TolovQilganYokiQilmaganTypeSerializer15_20()
    class Meta:
        model = Tolov
        fields = ('__all__')










