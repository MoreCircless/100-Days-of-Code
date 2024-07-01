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
AMADEUS_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2"
AMADEUS_FLIGHT_GET = "/shopping/flight-offers"

def get_amadeus_access_token(client_id, client_secret):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status() 
    return response.json()["access_token"]

access_token = get_amadeus_access_token(AMADEUS_KEY, AMADEUS_SECRET)

sheety_header = {
    "Authorization": SHEETY_KEY,
}
ama_par = {
    "origin": "MAD",
    "destination": "AMS",
    "departure": "2024-06-29",
    "adult": 1 
}

ama_header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}


flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SYD&destinationLocationCode=BKK&departureDate=2023-05-02&adults=1&nonStop=false&max=3"

flight = requests.get(url=f"{AMADEUS_ENDPOINT}{AMADEUS_FLIGHT_GET}?originLocationCode={ama_par['origin']}&destinationLocationCode={ama_par['destination']}&departureDate={ama_par['departure']}&adults={ama_par['adult']}&nonStop=false&max=1",
                    headers=ama_header)

flight = flight.json()
lastticket = flight["data"][0]["lastTicketingDate"]
departure = flight["data"][0]["itieraries"][0]["segments"][""]

print(flight)
print(lastticket)
print(departure)

# data = requests.get(url="https://api.sheety.co/69a2bf64984654c01496c348a088ac7b/copiaDeFlightDeals/prices", headers=header)

data = {
  "prices": [
    {
      "city": "Paris",
      "iataCode": "CDG",
      "lowestPrice": 54,
      "id": 2
    },
    {
      "city": "Tokyo",
      "iataCode": "HND",
      "lowestPrice": 485,
      "id": 3
    },
    {
      "city": "Amsterdam",
      "iataCode": "AMS",
      "lowestPrice": 50,
      "id": 4
    },
    {
      "city": "New York",
      "iataCode": "JFK",
      "lowestPrice": 240,
      "id": 5
    },
    {
      "city": "London",
      "iataCode": "LHR",
      "lowestPrice": 260,
      "id": 6
    }
  ]
}





# client = Client(TWILIOID, TWILIO_KEY)

# message = client.messages.create(
#     from_=f"{TWILIO_VIRTUAL_NUMBER}",
#     body="HOLA MUNDO",
#     to=f"{TWILIO_NUMBER}"
# )

# print(message)
# print(message.sid)
# # headers ={
# #     "Authorization": f"{SHEETY_KEY}",
    
# # }
# # response = requests.get(url=f"{SHEETY_ENDPOINT}", headers=headers)
# # print(response.text)