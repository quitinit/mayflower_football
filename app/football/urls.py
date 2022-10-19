from django.urls import path
from .views import player_view_all,player_view_one
urlpatterns = [
    path("players/",player_view_all ,name="get_all_players"),
    path("players/<int:id>",player_view_one ,name="get_one_player"),
   
]
