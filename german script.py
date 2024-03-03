 import requests


def get_phone_info(phone_number):
url = f"https://api.example.com/phone-info/{phone_number}"
response = requests.get(url)
data = response.json()


if data["success"]:
    print("Telefonnummer Informationen:")
    print(f"Telefonnummer: {phone_number}")
    print(f"Vorwahl: {data['area_code']}")
    print(f"Ort: {data['location']}")
    print(f"Anbieter: {data['provider']}")
else:
    print("Fehler beim Abrufen der Telefonnummer Informationen.")

phone_number = input("Gib die Telefonnummer ein: ")
get_phone_info(phone_number
