# destinations_app/urls.py
from django.urls import path
from .views import (
    # Frontend Views
    destination_list,
    destination_detail,
    destination_create,
    destination_update,
    destination_delete,

    # API Views
    TouristDestinationCreateView,
    TouristDestinationDetailView,
    TouristDestinationUpdateView,
    TouristDestinationDeleteView,
)

urlpatterns = [
    # Frontend URLs (HTML pages)
    path('', destination_list, name='destination-list'),
    path('<int:pk>/', destination_detail, name='destination-detail'),
    path('create/', destination_create, name='destination-create'),
    path('<int:pk>/update/', destination_update, name='destination-update'),
    path('<int:pk>/delete/', destination_delete, name='destination-delete'),

    # API URLs (JSON endpoints)
    path('api/create/', TouristDestinationCreateView.as_view(), name='api-create-destination'),
    path('api/<int:pk>/', TouristDestinationDetailView.as_view(), name='api-detail-destination'),
    path('api/<int:pk>/update/', TouristDestinationUpdateView.as_view(), name='api-update-destination'),
    path('api/<int:pk>/delete/', TouristDestinationDeleteView.as_view(), name='api-delete-destination'),
]