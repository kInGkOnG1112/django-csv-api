from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "videos"

router = DefaultRouter(trailing_slash=True)
router.register("", views.VideosViewSet, basename="videos")
urlpatterns = [
    path("videos/", include(router.urls)),
]
