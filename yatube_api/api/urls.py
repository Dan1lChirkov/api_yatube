from rest_framework import routers
from django.urls import include, path
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
