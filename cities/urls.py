from django.urls import path, include

from .views import HomePageView, SearchResultsView, CityListView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='cities'),
]