import json
import pytest

from football.models import Player

@pytest.mark.django_db
def create_player_success(client):
    players = Player.objects.all()
    assert len(players) == 0
    response = client.post(
        "/players/", {"name": "Michael", "location": "Berlin", "email": "michael@test.com"}
    )
    assert response.status_code == 201
    assert response.body ==  {"name": "Michael", "location": "Berlin", "email": "michael@test.com"}

