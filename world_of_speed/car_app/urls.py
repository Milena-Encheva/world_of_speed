from django.urls import path, include

from world_of_speed.car_app.views import CatalogueListView, CarCreateView, CarDetailView, CarEditView, CarDeleteView

urlpatterns = (
    path('catalogue/', CatalogueListView.as_view(), name='catalogue'),
    path('create/', CarCreateView.as_view(), name='create-car'),
    path(
        "<int:pk>/",
        include([
            path("details/", CarDetailView.as_view(), name="car_detail"),
            path("edit/", CarEditView.as_view(), name='car_edit'),
            path("delete/", CarDeleteView.as_view(), name='car_delete'),
            ]),
    ),
)
