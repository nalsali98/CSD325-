# api_test.py
# Name: Noor Al Salihi
# Assignment: Module 9 - API Connection Test

import requests

response = requests.get("http://www.google.com")
print("Status Code:", response.status_code)


