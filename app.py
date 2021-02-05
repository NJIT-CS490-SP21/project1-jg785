import requests
import os
import random
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

#Artist ID array
#Bad bunny, Maroon 5, Travis Scott 
artist_ID = ['4q3ewBCX7sLwd24euuV69X', '04gDigrS5kc9YWfZHwBETP',
              '0Y5tJX1MQlPlqiwlOH1tJY']
#Choose random artist ID
random_num = random.randint(0, 2)
my_artistID = artist_ID[random_num]

# base URL of all Spotify API endpoints - browse API
#BASE_URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

BASE_URL = 'https://api.spotify.com/v1/artists/' + my_artistID + '/top-tracks'

# actual GET request with proper header
response = requests.get(BASE_URL, 
                headers=headers,
                params={'market': 'US'})

#array of data from response
data = response.json()
#print(data)

#for loop to get 10 songs
for i in range(0,10):
    print(data['tracks'][i]['name'])