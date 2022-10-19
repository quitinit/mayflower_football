from rest_framework import serializers
from football.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Player
        fields = "__all__"
        read_only_fields = ('id', 'created_date', 'updated_date')
