from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Solemates API",
      default_version='v1',
      description="REST API for the running app Solemates",
      contact=openapi.Contact(email="admin@app.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('authentication.urls')),
   path('auth/', include('djoser.urls.jwt')),
   path('events/', include('events.urls')),
   path('users/', include('users.urls')),
   path('events/', include('events.urls')),
   path('wards/', include('wards.urls')),
   path('swagger<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]

