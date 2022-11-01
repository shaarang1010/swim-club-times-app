from rest_framework import serializers
from models import SwimEvent, SwimHeat, SwimmerEvent


class SwimEventSerializers(serializers.ModelSerializer):
    swim_meet = serializers.PrimaryKeyRelatedField(many=True, source='meet')

    class Meta:
        model = SwimEvent
        fields = ["name", "heats", "time", "swim_meet"]


class SwimHeatSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    heat_no = serializers.IntegerField()

    class Meta:
        model = SwimHeat
        fields = '__all__'


class SwimmerEventSerializer(serializers.ModelSerializer):
    athelte = serializers.PrimaryKeyRelatedField()
    event = serializers.PrimaryKeyRelatedField()
    heat = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = SwimmerEvent
        fields = '__all__'
