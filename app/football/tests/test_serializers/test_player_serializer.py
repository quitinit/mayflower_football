from football.serializers import PlayerSerializer

def test_valid_movie_serializer():
    valid_serializer_data = {
        "name": "Michael",
        "location": "Berlin",
        "email": "michael@test.com"
    }
    serializer = PlayerSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "name": "Michael",
        "email": "michael@test.com"
    }
    serializer = PlayerSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"location": ["This field is required."]}