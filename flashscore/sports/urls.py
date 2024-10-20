from django.urls import path
from .views import SportListView, SportDetailView, SportCreateView

urlpatterns = [
    path('', SportListView.as_view()),
    path('create/', SportCreateView.as_view())
]