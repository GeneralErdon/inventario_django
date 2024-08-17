from apps.base.router import CustomRouter

from apps.users.api.viewsets.user_viewset import UserModelViewset

router = CustomRouter()

router.register(r'user', UserModelViewset, basename='user-viewset')

urlpatterns = router.urls