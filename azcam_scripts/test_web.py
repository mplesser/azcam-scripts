import requests

for loop in range(1):

    r = requests.get(f"http://localhost:2403/instrument/get_filter")
    print(r.json()["message"])
