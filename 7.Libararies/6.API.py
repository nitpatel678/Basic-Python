import requests
import sys

# Check if the user provided a search term
if len(sys.argv) < 2:
    print("Usage: python script_name.py <search_term>")
    sys.exit()

# Proceed with the search if a search term is provided
response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(response.json())
