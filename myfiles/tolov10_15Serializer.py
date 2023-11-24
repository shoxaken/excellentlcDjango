from rest_framework import serializers
from myfiles.models import *


class Tolov10_15TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TolovQilganYokiQilmaganType_10_15
        fields = ('__all__')

class Tolov10_15Serializer(serializers.ModelSerializer):
    tolov_filter = Tolov10_15TypeSerializer()
    class Meta:
        model = Tolov10_15
        fields = ('__all__')