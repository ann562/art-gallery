# Project URLs (artgallery/urls.py)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # ✅ correct

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# App URLs (gallery/urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_piece_list, name='art_piece_list'),
    path('art/<int:pk>/', views.art_piece_detail, name='art_piece_detail'),
    path('report/', views.feedback_report, name='feedback_report'),
]