from django.urls import include, path
from django.contrib import admin
from back.router import router
from back.swagger import urlpatterns as docs_urlpatterns
from health.urls import urlpatterns as health_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include((health_urlpatterns, 'health'))),
    path('docs/', include((docs_urlpatterns, 'docs'))),
    path('api/', include(router.urls)),
]
