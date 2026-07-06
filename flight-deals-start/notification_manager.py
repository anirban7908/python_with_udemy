import os
from twilio.rest import Client
from  dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.TWILIO_SID = os.environ["TWILIO_SID"]
        self.TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
        self.from_num = os.environ['TWILIO_VIRTUAL_NUMBER']
        self.to_num = os.environ['TWILIO_WHATSAPP_NUMBER']

    # def send_to_whatsapp(self, data, destination):
    #     client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
    #     msg_body = f"Low Price alert! Only {data.price} to fly from {destination['origin_city_iata']} to {destination['city']}"
    #     message = client.messages.create(
    #         body=msg_body,
    #         from_=f"whatsapp:+15054085683",
    #         # from_=f"whatsapp:{self.from_num}",
    #         to=f"whatsapp:{self.to_num}",
    #     )
    def send_to_phone(self, data, destination):
        client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
        msg_body = f"Low Price alert! Only {data.price} to fly from {destination['origin_city_iata']} to {destination['city']}"
        message = client.messages.create(
            body=msg_body,
            from_="+15054085683",
            to=self.to_num,
        )