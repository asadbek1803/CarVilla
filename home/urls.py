from django.urls import path, include
from .views import Home, SearchViewSet, SearchCarAPIVEW
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("search/", SearchCarAPIVEW.as_view(), name="search"),
    path("all/cars/api/", SearchViewSet.as_view({'get':'list'}))

]