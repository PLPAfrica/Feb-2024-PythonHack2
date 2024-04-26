from django.conf.urls.static import static
from django.urls import path

from blogcast import settings
from . import views
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
from profiles import views as profile_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index/', views.index, name='index'),
    path('post/new/', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
