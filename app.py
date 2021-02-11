import requests
import os
import random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

load_dotenv(find_dotenv()) # This is to load your API keys from .env

################################
#KEYS
CLIENT_ID = os.getenv('SPOTIFY_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_SECRET')
GENIUS_TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')

################################

#Artist ID array
#Bad bunny, Maroon 5, Travis Scott 
artist_ID = ['4q3ewBCX7sLwd24euuV69X', '04gDigrS5kc9YWfZHwBETP',
              '0Y5tJX1MQlPlqiwlOH1tJY']
#Choose random artist ID
random_num = random.randint(0, 2)
my_artistID = artist_ID[random_num]

#Using Spotify API to fetch data
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
#BASE_URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

BASE_URL = 'https://api.spotify.com/v1/artists/' + my_artistID + '/top-tracks'

def get_data_spotify():
    #makes request to spotify api and returns array with artist name and song info.
    
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
    spotify = [artist_name, song_name, song_preview_url, image_url]
    return spotify
    
# spotify array from get_info()
spotify = get_data_spotify()
song_name = spotify[1]
artist_name = spotify[0]

################################
#Using GENIUS API to fetch data

def get_data_genius(song_name, artist_name):
    #send a GET request to genius api, gets response and returns the song lyrics.

    #Sending a GET request to the Genius API
    def request_song_info(song_name, artist_name):
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + GENIUS_TOKEN}
        search_url = base_url + '/search'
        data = {'q': song_name + ' ' + artist_name}
        response = requests.get(search_url, data=data, headers=headers)
    
        return response
    
    # Search for matches in the request response
    response = request_song_info(song_name, artist_name)
    json = response.json()
    remote_song_info = None
    
    #Iterate over the hits key in json
    for hit in json['response']['hits']:
        #look for an exact match using the artist_name variable.
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            #song is available in the API
            remote_song_info = hit
            break
        
    song_lyrics_url = None
    
    # Extract lyrics from URL if the song was found
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        song_lyrics_url = song_url
    
    return song_lyrics_url

################################
#Create server

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#connect URL with function
@app.route('/')
def hello_world():
    spotify_data = get_data_spotify()
    song_lyrics_url = get_data_genius(spotify_data[1], spotify_data[0])
    
    return render_template(
        "index.html",
        spotify_data = spotify_data,
        song_lyrics_url = song_lyrics_url
    )
    
app.run(
    #externally visible server
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    #will restart server when there are changes
    debug=True
)