from rest_framework import serializers, generics
from movies.models import movie,MOVIE_CATEGORIES, TIME_CHOICES, PRICE_CHOICES
from django.contrib.auth.models import User
from datetime import datetime


# --------------------------------------------------------------------
# Movie Serializer
# --------------------------------------------------------------------
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        #schedule_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
        fields = ['id','title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'trailer', 'description', 'owner']

# --------------------------------------------------------------------
# User Serializer
# --------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=movie.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'movies']

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        #representation['viewDateq'] = instance.created_at.strftime("%d-%m-%Y")
        return representation

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer