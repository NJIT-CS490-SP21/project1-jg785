import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

CLIENT_ID = os.getenv('ID')
CLIENT_SECRET = os.getenv('SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints - browse API
BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'

# actual GET request with proper header
response = requests.get(BASE_URL, 
                headers=headers, 
                params={'limit': 10})

#array of data from response
data = response.json()

#for loop to get 10 songs
for i in range(0,10):
    print(data['albums']['items'][i]['name'])
