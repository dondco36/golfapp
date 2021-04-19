from django.urls import path

from .views import ListRound, DetailRound

urlpatterns = [
    path('', ListRound.as_view()),
    path('<int:pk>/', DetailRound.as_view()),
]