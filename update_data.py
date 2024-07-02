import requests
import json

# Fetch data from external API
response = requests.get('https://api.example.com/data')
data = response.json()

# Update local JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)
