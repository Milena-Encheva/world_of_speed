from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.profile_app.forms import CreateProfileForm
from world_of_speed.profile_app.models import Profile
from world_of_speed.web.views import get_profile


# Create your views here.
class CreateProfileView(views.CreateView):

    form_class = CreateProfileForm
    queryset = Profile.objects.all()
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context


class DetailProfileView(views.DetailView):
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context

    def get_object(self, queryset=None):
        return get_profile()


class EditProfileView(views.UpdateView):
    model = Profile
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('detail_profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context

    def get_object(self, queryset=None):
        return get_profile()



