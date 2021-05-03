from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('show_movies/', views.Movies.as_view(), name="show_movies"),
    path('movie/<int:_id>/', views.MovieData.as_view(), name="movie"),
    path('search_movie', views.SearchMovie.as_view(), name="movie"),

    path('api-auth/', include('rest_framework.urls'))
]
