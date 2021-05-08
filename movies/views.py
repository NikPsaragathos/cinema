from django.contrib.auth.models import User
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
from rest_framework import permissions, generics

from movies.models import movie
from movies.permissions import IsOwnerOrReadOnly
from movies.serializers import MovieSerializer, UserSerializer

# --------------------------------------------------------------------
# Movie Api View
# --------------------------------------------------------------------

class MovieList(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    filter_fields = (['title', 'categoryId', 'viewDate', 'timeId', 'priceId'])
    search_fields = [ 'title', 'categoryId', 'viewDate', 'timeId', 'priceId']
    ordering_fields = ['title', 'categoryId', 'viewDate', 'timeId']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# --------------------------------------------------------------------
# User Api View
# --------------------------------------------------------------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
