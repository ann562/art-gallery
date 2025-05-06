from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # 👈 includes your app
]

# ✅ Append media URL support in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
