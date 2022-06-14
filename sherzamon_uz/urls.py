
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import *
from django.urls import re_path as url
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
