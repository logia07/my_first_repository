import requests


api_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(api_url)

coordinates = response.json().get("iss_position")

formatted_coordinates = f"{coordinates['longitude']}%2C{coordinates['latitude']}"

map_url = f"https://yandex.com/maps/?ll={formatted_coordinates}&z=10"

print(map_url)