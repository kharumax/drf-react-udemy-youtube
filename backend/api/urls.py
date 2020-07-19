from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()
router.register("videos",VideoViewSet)

app_name="api"
urlpatterns = [
    path('create/',CreateUserView.as_view(),name="crate"),
    path('users/',UserListView.as_view(),name="list"),
    path('users/<str:pk>/',UserDetailView.as_view(),name="detail"),
    path('users/update/<str:pk>/',UserUpdateView.as_view(),name="update"),
    path('',include(router.urls)),
]