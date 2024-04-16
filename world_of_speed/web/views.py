from django.shortcuts import render
from world_of_speed.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    user_profile = get_profile()
    context = {'user_profile': user_profile}

    return render(request, 'web/index.html', context)

