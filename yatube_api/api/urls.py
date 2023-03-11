from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView
                                            )

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register(
    r'v1/posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/jwt/create/', TokenObtainPairView.as_view()),
    path('v1/jwt/refresh/', TokenRefreshView.as_view()),
    path('v1/jwt/verify/', TokenVerifyView.as_view()),
]
