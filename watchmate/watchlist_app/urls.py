from django.urls import include, path

from watchlist_app.views import movie_detail, movie_list

urlpatterns = [
    path("list/", movie_list, name="movie-list"),
     path("<int:pk>", movie_detail, name="movie-detail"),
]
