from rest_framework import serializers
from myfiles.models import *



class TolovQilganYokiQilmaganTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TolovQilganYokiQilmaganType_25_30
        fields = '__all__'

class Tolov25_30Serializer(serializers.ModelSerializer):
    tolov_filter = TolovQilganYokiQilmaganTypeSerializer()
    class Meta:
        model = Tolov25_30
        fields = ('__all__')
