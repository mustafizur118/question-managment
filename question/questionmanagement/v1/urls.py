from django.urls import path
from . import views

urlpatterns = [
    path('user-count/', views.user_favorite_read_count, name='user-count'),
    path('filter-questions/', views.filter_questions, name='filter-questions'),
]
