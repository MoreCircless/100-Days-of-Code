from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests


load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_KEY = os.getenv("SHEETY_AUTH")
TWILIOID = os.getenv("TWILIOID")
TWILIO_KEY = os.getenv("TWILIOKEY")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")


client = Client(TWILIOID, TWILIO_KEY)

message = client.messages.create(
    from_=f"{TWILIO_VIRTUAL_NUMBER}",
    body="HOLA MUNDO",
    to=f"{TWILIO_NUMBER}"
)

print(message)
print(message.sid)
# headers ={
#     "Authorization": f"{SHEETY_KEY}",
    
# }
# response = requests.get(url=f"{SHEETY_ENDPOINT}", headers=headers)
# print(response.text)