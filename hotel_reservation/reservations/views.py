from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages
from twilio.rest import Client

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def send_sms_notification(name, phone_number):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    # Ensure the phone number is in E.164 format
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=f"Dear {name}, your reservation has been successfully booked!",
            from_=twilio_phone_number,
            to=phone_number
        )
        return message.sid
    except Exception as e:
        # Handle exceptions (e.g., invalid phone number)
        print(f"Error sending SMS: {str(e)}")
        return None

# def reservation_create(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('reservation_list')
#     else:
#         form = ReservationForm()
#     return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # Send SMS notification
            send_sms_notification(reservation.name, reservation.phone_number)

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