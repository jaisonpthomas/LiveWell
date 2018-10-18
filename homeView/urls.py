from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/<dateVal>', views.HealthDataDetailView.as_view()),
    # path('/api/'),
]
