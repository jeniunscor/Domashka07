from django.urls import path
from .views import *

urlpatterns=[
    path('items/',ItemListView.as_view()),
    path('items/<int:pk>/',ItemDetailView.as_view())

    ]