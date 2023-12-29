from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages
from twilio.rest import Client
from .send_sms import sendsms


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # Send SMS notification
            sendsms(reservation.name, reservation.phone_number)

            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_redirect(request):
    return redirect('reservation_list')

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    messages.success(request, 'Reservation updated successfully.')
    return render(request, 'reservations/reservation_form.html', {'form': form, 'reservation': reservation})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    messages.success(request, 'Reservation deleted successfully.')
    return redirect('reservation_list')