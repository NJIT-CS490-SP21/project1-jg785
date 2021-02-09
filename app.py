import requests
import os
import random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

################################
#Using Spotify API to fetch data

load_dotenv(find_dotenv()) # This is to load your API keys from .env

#KEYS
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

#array of data from response - fetched top tracks
data = response.json()
#print(data)

#to get songs - data['tracks'][i]['name']
#random - to get a random song from 1-10
random_song_num = random.randint(0, 9)

artist_name = data['tracks'][random_song_num]['artists'][0]['name']
song_name = data['tracks'][random_song_num]['name']
song_preview_url = data['tracks'][random_song_num]['preview_url']
image_url = data['tracks'][random_song_num]['album']['images'][1]['url']

#array with all information to be displayed
#spotify = [artist_name, song_name, song_preview_url, image_url]

#print(artist_name, song_name, preview_url, image_url)
################################
#Create server

app = Flask(__name__)

#connect URL with function
@app.route('/')
def hello_world():
    print('Updated printline')
    return render_template(
        "index.html",
        artist_name = artist_name,
        song_name = song_name,
        song_preview_url = song_preview_url,
        image_url = image_url
    )
    
app.run(
    #externally visible server
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    #will restart server when there are changes
    debug=True
)