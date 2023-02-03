import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/Property", json={"area": 145,
                                                  "property-type": "house",
                                                  "rooms-number": 5,
                                                  "zip-code": 4000,
                                                  "land-area": 58,
                                                  "garden": True,
                                                  "garden-area": 21,
                                                  "equipped-kitchen": True,
                                                  "full-address": "Rue des wallons 230",
                                                  "swimming-pool": True,
                                                  "furnished": True,
                                                  "open-fire": True,
                                                  "terrace": True,
                                                  "terrace-area": 45,
                                                  "facade-number": 4,
                                                  "building-state": "Good"})

print(response.json())