from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Destination, Accommodation, Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from .forms import DestinationForm, AccommodationForm, ActivityForm

# Destinations

def homepage(request):
    return render(request, 'locations/homepage.html')

class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination

class DestinationDetailView(DetailView):
    model = Destination

class DestinationCreateView(CreateView):
    model = Destination
    fields = ['name', 'country', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination_dict = {
            'name': '',
            'country': '',
            'description': '',
        }
        context['destination_dict'] = destination_dict
        context['activities'] = []
        context['accommodations'] = []
        return context

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
        return reverse_lazy('locations:destination_detail', args=[self.object.id])

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accommodation_dict = {
            'name': '',
            'price_per_night': '0.00',
            'destination': '',
            'destination_name': '',
            'country': '',
        }
        context['accommodation_dict'] = accommodation_dict
        context['destinations'] = list(Destination.objects.all().values('id', 'name','country'))
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Accommodation "{self.object.name}" has been created.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:accommodation_detail', args=[self.object.id])

class AccommodationUpdateView(UpdateView):
    model = Accommodation
    form_class = AccommodationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Accommodation "{self.object.name}" has been updated.'
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accommodation = self.object
        accommodation_dict = model_to_dict(accommodation)

        accommodation_dict['price_per_night'] = str(accommodation.price_per_night)
        accommodation_dict['destination'] = accommodation.destination.id
        accommodation_dict['destination_name'] = accommodation.destination.name
        accommodation_dict['country'] = accommodation.destination.country.upper()

        context['accommodation_dict'] = accommodation_dict
        context['destinations'] = list(Destination.objects.all().values('id', 'name'))

        return context

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
    form_class = ActivityForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        activity_dict = {
            'name': '',
            'price': '0.00',
            'destination': '',
        }
        
        context['activity_dict'] = activity_dict
        context['destinations'] = list(Destination.objects.all().values('id', 'name'))
        
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Activity "{self.object.name}" has been created.')
        return response

    def get_success_url(self):
        return reverse_lazy('locations:activity_detail', args=[self.object.id])

class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Activity "{self.object.name}" has been updated.'
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity = self.object
        activity_dict = model_to_dict(activity)

        activity_dict['price'] = str(activity.price)
        activity_dict['destination'] = activity.destination.id
        activity_dict['destination_name'] = activity.destination.name
        activity_dict['country'] = activity.destination.country.upper()

        context['activity_dict'] = activity_dict
        context['destinations'] = list(Destination.objects.all().values('id', 'name'))

        return context

    def get_success_url(self):
        return reverse_lazy('locations:activity_detail', args=[self.object.id])

class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy('locations:activity_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             f'Activity "{self.object.name}" has been successfully deleted.')
        return response
