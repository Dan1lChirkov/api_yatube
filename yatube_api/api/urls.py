from rest_framework import routers
from django.urls import include, path
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, api_comment, api_comment_detail

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/', api_comment),
    path('posts/<int:post_id>/comments/<int:comment_id>/', api_comment_detail),
]
