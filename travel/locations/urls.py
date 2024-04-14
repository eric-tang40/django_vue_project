from django.urls import path

from . import views

app_name = "locations"

urlpatterns = [
    path("locations/", views.DestinationListView.as_view(), name="destination_list"),
    path("locations/<int:pk>/", views.DestinationDetailView.as_view(), name="destination_detail"),
    path("locations/new/", views.DestinationCreateView.as_view(), name="destination_create"),
    path("locations/update/<int:pk>/", views.DestinationUpdateView.as_view(), name="destination_update"),
    path("locations/delete/<int:pk>/", views.DestinationDeleteView.as_view(), name="destination_delete"),

    path("accommodations/", views.AccommodationListView.as_view(), name="accommodation_list"),
    path("accommodations/<int:pk>/", views.AccommodationDetailView.as_view(), name="accommodation_detail"),
    path("accommodations/new/", views.AccommodationCreateView.as_view(), name="accommodation_create"),
    path("accommodations/update/<int:pk>/", views.AccommodationUpdateView.as_view(), name="accommodation_update"),
    path("accommodations/delete/<int:pk>/", views.AccommodationDeleteView.as_view(), name="accommodation_delete"),

    path("activities/", views.ActivityListView.as_view(), name="activity_list"),
    path("activities/<int:pk>/", views.ActivityDetailView.as_view(), name="activity_detail"),
    path("activities/new/", views.ActivityCreateView.as_view(), name="activity_create"),
    path("activities/update/<int:pk>/", views.ActivityUpdateView.as_view(), name="activity_update"),
    path("activities/delete/<int:pk>/", views.ActivityDeleteView.as_view(), name="activity_delete"),
]