import pytest
from football.models import Location
#this is a database fixture that reverts changes to the database
@pytest.mark.django_db
def test_init_location():
    location = Location(name="Berlin")
    location.save()
    assert location.name == "Berlin"
    #player = Player()