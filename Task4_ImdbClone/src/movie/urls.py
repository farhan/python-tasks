from django.contrib import admin
from django.urls import path
from .views import *

app_name='movie'

urlpatterns = [
    path('', MovieList.as_view(), name="movie_list"),
    path('<int:pk>', MovieDetail.as_view(), name="movie_detail"),
    path('category/<str:category>', MovieCategory.as_view(), name="movie_category"),
    path('language/<str:language>', MovieLanguage.as_view(), name="movie_language"),
    path('search/', MovieSearch.as_view(), name="movie_search"),
    path('year/<int:year>', MovieYear.as_view(), name="movie_year"),
]
