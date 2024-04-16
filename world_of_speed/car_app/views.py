from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.car_app.forms import CarCreationForm
from world_of_speed.car_app.models import Car
from world_of_speed.profile_app.models import Profile
from world_of_speed.web.views import get_profile


class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


class CarCreateView(views.CreateView):
    queryset = Car.objects.all()
    form_class = CarCreationForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context


class CatalogueListView(views.ListView):
    queryset = Car.objects.all()
    template_name = 'car/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context


class CarDetailView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'car/car-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context


class CarEditView(views.UpdateView):
    queryset = Car.objects.all()
    template_name = 'car/car-edit.html'
    fields = ('type', 'model', 'year', 'image_URL', 'price')
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context


class CarDeleteView(ReadonlyViewMixin, views.DeleteView):
    model = Car
    template_name = "car/car-delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.first()
        context['user_profile'] = user_profile
        return context

    def get_form_class(self):
        return modelform_factory(
            self.model,
            fields=('type', 'model', 'year', 'price', 'image_URL'),
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.get_object()
        return kwargs
