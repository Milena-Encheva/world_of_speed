from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('world_of_speed.web.urls')),
    path('profile/', include('world_of_speed.profile_app.urls')),
    path('car/', include('world_of_speed.car_app.urls')),
]
