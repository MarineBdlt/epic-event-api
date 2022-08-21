from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contracts.views import ContractViewSet
from events.views import EventViewSet
from clients.views import ClientViewSet
from auth_app.views import UserViewSet

admin.site.site_header = 'Epic Event CER'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'events', EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path("api/account/", include(router.urls)),
]
