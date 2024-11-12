from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# Bu yerda views dagi malumotlar
from .views import (
    HelloApiView,
    HelloViewSet,
    UserProfileViewSet,
    LoginViewSet,
    UserProfileFeedViewSet
    )

# Tayyor bo'lgan django rest api
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet, basename="profile")
router.register('login', LoginViewSet, basename="login")
router.register('feed', UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()), #
    path('', include(router.urls)),
]