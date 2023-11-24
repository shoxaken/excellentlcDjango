from rest_framework import serializers
from myfiles.models import *


class Tolov5_10TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TolovQilganYokiQilmaganType_5_10
        fields = ('__all__')

class Tolov5_10Serializer(serializers.ModelSerializer):
    tolov_filter = Tolov5_10TypeSerializer()
    class Meta:
        model = Tolov5_10
        fields = ('__all__')
