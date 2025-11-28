# astronauts.py
# Name: Noor Al Salihi
# Assignment: Module 9 - Astronaut API

import requests
import json

# API URL from the tutorial
url = "http://api.open-notify.org/astros.json"

# Test connection
response = requests.get(url)
print("Connection Status:", response.status_code)

# Unformatted response
print("\nRaw Response:")
print(response.text)

# Formatted output
data = response.json()

print("\nFormatted Output:")
print("Number of astronauts currently in space:", data["number"])
print("List of astronauts:")

for person in data["people"]:
    print("-", person["name"])


