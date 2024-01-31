from django.urls import include, path
from back.router import router
from back.swagger import urlpatterns as docs_urlpatterns

urlpatterns = [
    path('docs/', include((docs_urlpatterns, 'docs'))),
    path('api/', include(router.urls)),
]
