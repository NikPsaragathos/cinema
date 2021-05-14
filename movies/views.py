import django_filters
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from movies.models import movie
# Create your views here.
from rest_framework import permissions, generics, status
from movies.models import movie
from movies.permissions import IsOwnerOrReadOnly
from movies.serializers import MovieSerializer, UserSerializer
from rest_framework import filters
from django_filters import rest_framework as filters
from rest_framework import filters
import django_filters
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .resources import MovieResource



class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter( field_name="title",label=" ΤΙΤΛΟΣ", lookup_expr='icontains')
    categoryId =django_filters.NumberFilter( field_name='categoryId',label="ΚΑΤΗΓΟΡΙΑ", lookup_expr='gte')
    viewDate= django_filters.NumberFilter( field_name='viewDate', label="ΗΜΕΡΟΜΗΝΙΑ ΠΡΟΒΟΛΗΣ", lookup_expr='exact')
    timeId = django_filters.NumberFilter( field_name='timeId', label="ΩΡΑ ΠΡΟΒΟΛΗΣ", lookup_expr='exact')
    priceId = django_filters.NumberFilter( field_name='priceId', label="ΤΙΜΗ ΕΙΣΗΤΗΡΙΟΥ", lookup_expr='exact')

class Meta:
     model = movie
     fields = [ 'title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'description', 'trailer', 'owner']



# --------------------------------------------------------------------
# Movie Api View returns a list of full movies
# --------------------------------------------------------------------

class MovieList(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    # --------------------------------------------------------------------
    # Movie Api View returns a list of full movies
    # CREATE, DELETE, UPDATE only authenticated χρήστης.
    # The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users
    # will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.
    # This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write
    # permissions to authenticated users.
    # --------------------------------------------------------------------

    filter_class= MovieFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = (['title', 'categoryId', 'viewDate', 'timeId', 'priceId'])
    search_fields = ['title', 'categoryId', 'viewDate', 'timeId', 'priceId']
    ordering_fields = ('title', 'categoryId', 'timeId', 'priceId')



#Override την default μέθοδο create the class and store in the field owner the user who wasn't register
def perform_create(self, serializer):
    serializer.save( owner=self.request.user )

def export(request):
    movie_resource = MovieResource
    dataset = movie_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="movie.csv"'
    #response = HttpResponse(dataset.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="movie.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer

# Read permissions are allowed to any request, Write permissions are only allowed to the owner
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


# --------------------------------------------------------------------
# #above is the method who is more analytic and time consuming
# --------------------------------------------------------------------


# @api_view(['GET', 'POST'])
# def food_list(request, format=None):
#    #List all foods, or create a new food.
#   if request.method == 'GET':
#        foods = Food.objects.all()
#        serializer = FoodSerializer(foods, many=True)
#        return Response(serializer.data)

#    elif request.method == 'POST':
#       serializer = FoodSerializer(data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def food_detail(request, pk, format=None):
# Retrieve, update or delete a food instance.
#    try:
#        food = Food.objects.get(pk=pk)
#    except Food.DoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = FoodSerializer(food)
#        return Response(serializer.data)

#    elif request.method == 'PUT':
#       serializer = FoodSerializer(food, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == 'DELETE':
#       food.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

