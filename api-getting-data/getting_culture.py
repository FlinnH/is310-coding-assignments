# imports
import requests
from dotenv import load_dotenv
import os
import json
import pyeuropeana.apis as apis

# Get Stranger Things Characters 
print("HawAPI — Stranger Things Characters")
url = "https://hawapi.theproject.id/api/v1/characters"

response = requests.get(url)
print(f"Status code: {response.status_code}")

data = response.json()

# Each character has: uuid, first_name, last_name, nicknames, status, etc.
print(f"Total characters returned: {len(data)}\n")

# Print all character names from the response
print("Characters returned:")
for character in data:
    full_name = f"{character['first_name']} {character['last_name']}"
    print(f"  - {full_name}")

# Pick one character to search in Europeana
chosen = data[0]
chosen_name = f"{chosen['first_name']} {chosen['last_name']}"
print(f"\nChosen character for Europeana search: {chosen_name}")

# Europeana — Search for Related Items 
print("\nEuropeana Search")

# Load Europeana API key 
load_dotenv() 
europeana_api_key = os.getenv("EUROPEANA_API_KEY")

# Search Europeana for the chosen character name
result = apis.search(query=chosen_name)

print(f"Search query: '{chosen_name}'")
print(f"Total results found in Europeana: {result['totalResults']}")

# If no results, just search for Stranger Things instead
if result['totalResults'] == 0:
    print("No results for that name. Searching 'Stranger Things' instead...")
    result = apis.search(query="Stranger Things")
    print(f"Total results for 'Stranger Things': {result['totalResults']}")

# Print a preview of the first few items (for debugging)
items = result.get('items', [])
print(f"\nPreview of first {min(3, len(items))} Europeana item(s):")
for item in items[:3]:
    title = item.get('title', ['No title'])[0]
    provider = item.get('dataProvider', ['Unknown'])[0]
    print(f"  Title: {title}")
    print(f"  Provider: {provider}\n")

# Save Europeana Results to JSON 
print("\nSaving Europeana Data")

# Filter out the API key from results before saving (for debugging)
safe_result = {k: v for k, v in result.items() if k != 'apikey'}

output_filename = "hawapi_europeana_data.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(safe_result, f, indent=2, ensure_ascii=False)

# Debugging
print(f"Saved Europeana results to: {output_filename}")
print(f"Total items saved: {len(items)}")