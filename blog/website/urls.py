from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.user_views import *
from .views.article_views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('add_article/', add_article, name='add_article'),
    path('delete_article/<int:pk>', delete_article, name='delete_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('update_article/<int:pk>', update_article, name='update_article'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
