from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Destination, Accommodation, Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from .forms import DestinationForm

# Destinations

class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination

class DestinationDetailView(DetailView):
    model = Destination

class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Destination "{self.object.name}" has been created.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:destination_detail', args=[self.object.id])


class DestinationUpdateView(UpdateView):
    model = Destination
    form_class = DestinationForm
    template_name = 'destinations/destination_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Destination "{destination_name}" has been updated.'.format(
                destination_name=self.object.name
            ),
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination_dict = model_to_dict(self.object)
        
        destination_dict['country'] = destination_dict['country'].upper()
        context['destination_dict'] = destination_dict
        context['activities'] = list(self.object.activity_set.all().values('name', 'price'))
        context['accommodations'] = list(self.object.accommodation_set.all().values('name', 'price_per_night'))

        print("context", context)
        return context

    def get_success_url(self):
        return reverse_lazy('locations:destination_detail', kwargs={'pk': self.object.pk})

class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = reverse_lazy('locations:destination_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Destination "{self.object.name}" has been deleted.')
        return response

# Accommodations

class AccommodationListView(ListView):
    model = Accommodation

class AccommodationDetailView(DetailView):
    model = Accommodation

class AccommodationCreateView(CreateView):
    model = Accommodation
    fields = ['name', 'destination', 'price_per_night']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Accommodation "{self.object.name}" has been created.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:accommodation_detail', args=[self.object.id])

class AccommodationUpdateView(UpdateView):
    model = Accommodation
    fields = ['name', 'destination', 'price_per_night']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Accommodation "{self.object.name}" has been updated.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:accommodation_detail', args=[self.object.id])

class AccommodationDeleteView(DeleteView):
    model = Accommodation
    success_url = reverse_lazy('locations:accommodation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Accommodation "{self.object.name}" has been deleted.')
        return response

# Activities

class ActivityListView(ListView):
    model = Activity

class ActivityDetailView(DetailView):
    model = Activity

class ActivityCreateView(CreateView):
    model = Activity
    fields = ['name', 'destination', 'price']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Activity "{self.object.name}" has been created.')
        return response

class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['name', 'destination', 'price']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Activity "{self.object.name}" has been successfully updated.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:activity_detail', kwargs={'pk': self.object.pk})

class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy('locations:activity_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Activity "{self.object.name}" has been successfully deleted.')
        return response
