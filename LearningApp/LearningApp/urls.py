
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('course/', include('course.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)