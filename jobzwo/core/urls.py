from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from core import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'400/', views.raise400),
        url(r'403/', views.raise403),
        url(r'500/', views.raise500),
    ]
