# api_request.py
# This script makes a request to a public API
# and handles possible errors using try/except

import requests

# This is a free public API we will request data from
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Try to request data from the API
    response = requests.get(url, timeout=5)

    # Check if the request was successful
    response.raise_for_status()

    # Convert the response to JSON
    data = response.json()

    # Display part of the data
    print("API request successful!")
    print("Post title:", data["title"])

# If the request takes too long
except requests.exceptions.Timeout:
    print("Error: The request timed out. Try again later.")

# If the internet connection fails
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")

# If the server returns a bad response
except requests.exceptions.HTTPError:
    print("Error: The API returned a bad response.")

# Catch any other unexpected error
except Exception as e:
    print("Unexpected error occurred:", e)