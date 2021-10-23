# from rest_framework import routers
# from .views import WorkViewSet, CommentsViewSet
#
# router = routers.SimpleRouter()
# router.register('artworks', WorkViewSet, basename='artworks')  # register "Work viewSet" in router in url path
# router.register('comments', CommentsViewSet, basename='comments')  # register "Comments viewSet" in router in url path
#
# urlpatterns = []
# urlpatterns += router.urls  # Add registered "urls" to the main routing.

from django.urls import path, include
from .views import *

app_name = 'artworks'
urlpatterns = [
    path('artworks/', WorkCreateView.as_view()),  # route Work view class.
    path('comments/', CommentsCreateView.as_view()),
]
