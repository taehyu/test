from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'user', UserViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = router.urls

