from rest_framework import serializers
from myfiles.models import *

class Tolov20_25TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TolovQilganYokiQilmaganType_20_25
        fields = ('__all__')


class Tolov20_25Serializer(serializers.ModelSerializer):
    tolov_filter = Tolov20_25TypeSerializer()
    class Meta:
        model = Tolov20_25
        fields = ('__all__')