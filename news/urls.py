from django.urls import path
from .views import upload_article, search_articles

urlpatterns = [
    path('upload/', upload_article),
    path('search/', search_articles),
]
