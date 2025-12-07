# destinations_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
import requests
from .forms import TouristDestinationForm



# Frontend Views (Traditional Django Views)
def destination_list(request):
    """Display all tourist destinations"""
    destinations = TouristDestination.objects.all()
    return render(request, 'destinations_app/destination_list.html', {
        'destinations': destinations
    })


def destination_detail(request, pk):
    """Display single destination details"""
    destination = get_object_or_404(TouristDestination, pk=pk)
    return render(request, 'destinations_app/destination_detail.html', {
        'destination': destination
    })


def destination_create(request):
    """Create new destination with form"""
    if request.method == 'POST':
        form = TouristDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination created successfully!')
            return redirect('destination_list')
    else:
        form = TouristDestinationForm()

    return render(request, 'destinations_app/destination_form.html', {
        'form': form,
        'title': 'Create New Destination'
    })


def destination_update(request, pk):
    """Update existing destination"""
    destination = get_object_or_404(TouristDestination, pk=pk)

    if request.method == 'POST':
        form = TouristDestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination updated successfully!')
            return redirect('destination_list')
    else:
        form = TouristDestinationForm(instance=destination)

    return render(request, 'destinations_app/destination_form.html', {
        'form': form,
        'title': 'Update Destination'
    })


def destination_delete(request, pk):
    """Delete destination"""
    destination = get_object_or_404(TouristDestination, pk=pk)

    if request.method == 'POST':
        destination.delete()
        messages.success(request, 'Destination deleted successfully!')
        return redirect('destination_list')

    return render(request, 'destinations_app/destination_confirm_delete.html', {
        'destination': destination
    })


# API Views (DRF Views - Keep your existing ones)
class TouristDestinationCreateView(generics.ListCreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    permission_classes = (AllowAny,)


class TouristDestinationDetailView(generics.RetrieveAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer


class TouristDestinationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer


class TouristDestinationDeleteView(generics.DestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer