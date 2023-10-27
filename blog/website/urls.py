from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_article/', views.add_article, name='add_article'),
    path('delete_article/<int:pk>', views.delete_article, name='delete_article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('update_article/<int:pk>', views.update_article, name='update_article'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
