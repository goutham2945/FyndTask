from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, queryset=Genre.objects.all(), slug_field='name')

    class Meta:
        model = Movie
        fields = ('popularity', 'director', 'genre', 'score','name')



