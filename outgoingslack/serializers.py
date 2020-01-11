from .models import OutGoingSlack
from rest_framework import serializers

class SlackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutGoingSlack
        fields = '__all__'