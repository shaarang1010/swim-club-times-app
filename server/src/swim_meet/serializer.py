from rest_framework import serializers
from models import SwimMeet


class SwimMeetSerializer(serializers.Modelserializers):
    class Meta:
        model = SwimMeet
        fields = '__all__'
