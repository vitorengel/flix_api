from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateLitsView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyVies.as_view(), name='actor-detail-view'),
]
