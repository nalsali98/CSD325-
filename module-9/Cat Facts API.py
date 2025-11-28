# cat_facts.py
# Name: Noor Al Salihi
# Assignment: Module 9 - Custom API Program

import requests
import json

url = "https://catfact.ninja/fact"

# Test connection
response = requests.get(url)
print("Connection Status:", response.status_code)

# Unformatted response
print("\nRaw JSON Text:")
print(response.text)

# Formatted Response
data = response.json()

print("\nFormatted Output:")
print("Random Cat Fact:")
print("-", data["fact"])
print("Length:", data["length"])
