from django.conf.urls import url
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'sign-up', SignUpViewSet, base_name='sign-up')
router.register(r'log-in', LoginViewSet, base_name='log-in')
router.register(r'profile-viewset', UserProfileViewSet)
router.register(r'following-viewset', UserFollowingViewSet)

urlpatterns = [
    url(r'^change-password-view/', ChangePasswordApiView.as_view()),
]

urlpatterns += router.urls
