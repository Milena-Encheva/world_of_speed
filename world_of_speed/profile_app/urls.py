from django.urls import path

from world_of_speed.profile_app.views import CreateProfileView, DetailProfileView, DeleteProfileView, EditProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', DetailProfileView.as_view(), name='detail_profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
)
