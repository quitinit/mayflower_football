
# Create your views here.
from .models import Player

from django.http import JsonResponse

from django.core import serializers
from django.shortcuts import get_object_or_404

def player_view_all(request):
    if request.method == "GET":
        players = Player.objects.all()
        data =serializers.serialize('json', Player.objects.all(), fields=('user','location'))
        return JsonResponse(data,safe=False)
        #serializer = PlayerSerializer(players)
        #return JSONRenderer().render(serializer.data)
        #return serializer.render()

def player_view_one(request,id):
    if request.method == "GET":
        response = get_object_or_404(Player,pk=id)
        if response:
            data = {"name": response.user.username}
        return JsonResponse(data,safe=False)
