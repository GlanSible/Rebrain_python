from django.urls import path
from .views import ServerViewSetShort, ServerViewSet, ServerDetailView, ServerAddView, ExtendedServerInfoView, ExtendedServerAddView


urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('servers/add-extended', ExtendedServerAddView.as_view()),
    path('servers/status', ServerViewSetShort.as_view()),
    path('servers/extended-info', ExtendedServerInfoView.as_view())
]
