import os, requests
from dotenv import load_dotenv

# load the operating system .env file where i stored my access keys -
# I don't want this in my script for security reason
load_dotenv()
API_KEY = os.getenv("API_FOOTBALLKEY")

# we create the headers - this is how I authenticate with the API (kinda like showing ID at the door)
# in this case we're calling the /teams endpoint.

url = "https://v3.football.api-sports.io/teams?country=England"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "v3.football.api-sports.io/"
}

response = requests.get(url, headers=headers)

# pipeline would just sit there and fail without telling you it failed if we dont have this.
if response.status_code != 200:
    raise Exception(f"Request has failed: {response.status_code} - {response.text}")

data = response.json()
print(data)