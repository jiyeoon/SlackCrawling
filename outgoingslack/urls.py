from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('slack', views.SlackViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('list', views.post_list, name = 'post_list'),
]