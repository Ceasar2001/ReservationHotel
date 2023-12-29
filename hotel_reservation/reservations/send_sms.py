from sinch import Client
from .models import Reservation
from .forms import ReservationForm

def sendsms(name, phone_number):
    sinch_client = Client(
        key_id="7a2d48f3-e4b4-43dd-a4be-da0abec9ff69",
        key_secret="j7KWy9Jah1edRNeBocd6jmxS3V",
        project_id="7616ed10-a502-4789-a8c0-4886fb0a8b43"
    )

    send_batch_response = sinch_client.sms.batches.send(
        body=f"Dear {name}, your reservation has been successfully booked fuck you!",
        to=[ phone_number ],
        from_="447520652178",
        delivery_report="none"
    )
