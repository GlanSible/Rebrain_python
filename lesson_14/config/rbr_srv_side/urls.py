from django.urls import path
from .views import ServerViewSet, ServerDetailView, ServerAddView


urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
]
