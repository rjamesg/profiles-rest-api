from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name='hello-viewset')

## passing in a URL pattern for API Views. Different to ViewSet.
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
