from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #movies
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>/', views.MovieDetail.as_view()),
    #users
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    #path('admin/', admin.site.urls),
    url(r'^export-exl/$', views.export, name='export'),
    url(r'^export-csv/$', views.export, name='export'),
]