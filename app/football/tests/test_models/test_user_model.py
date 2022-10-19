import pytest
from django.contrib.auth import get_user_model
from football.models import Location,Player
#this is a database fixture that reverts changes to the database
@pytest.mark.django_db
def test_create_normal_user():
    User = get_user_model()
    user = User.objects.create_user(email='normal@user.com', password='foo',username="normaluser")
    assert user.email == 'normal@user.com'
    assert user.is_active
    assert not user.is_superuser

@pytest.mark.django_db
def test_create_normal_player():
    User = get_user_model()
    user = User.objects.create_user(email='normal@user.com', password='foo',username="normaluser")
    location = Location(name="Berlin")
    player = Player(user=user,location=location)
    #player.save()
    assert player.user.email == "normal@user.com"
    assert player.location.name == "Berlin"
    #player = Player()