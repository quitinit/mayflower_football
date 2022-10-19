from football.serializers import PlayerSerializer

def valid_movie_serializer():
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


