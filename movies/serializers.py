from rest_framework import serializers
from movies.models import movie,MOVIE_CATEGORIES, TIME_CHOICES, PRICE_CHOICES
from django.contrib.auth.models import User


# --------------------------------------------------------------------
# Movie Serializer
# --------------------------------------------------------------------
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ['id','title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'trailer', 'description', 'owner']

# --------------------------------------------------------------------
# User Serializer
# --------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=movie.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'movies']


