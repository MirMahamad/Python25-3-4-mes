from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('book.urls')),
    path('', include('tv_shows.urls')),
    path('', include('parser_app.urls')),
    path('', include('hw_custom_user.urls')),
    path('', include('cloth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
