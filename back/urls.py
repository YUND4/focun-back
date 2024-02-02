from django.urls import include, path
from django.contrib import admin
from back.swagger import urlpatterns as docs_urlpatterns
from health.urls import urlpatterns as health_urlpatterns
from users.urls import urlpatterns as users_urlpatterns
from jobs.urls import urlpatterns as jobs_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include((health_urlpatterns, 'health'))),
    path('docs/', include((docs_urlpatterns, 'docs'))),
    path('', include((users_urlpatterns, 'users'))),
    path('', include((jobs_urlpatterns, 'jobs'))),
]
