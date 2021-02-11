Project 1, Mileston 1 & 2 - Jhon Garcia

Programs used to do this project: Python, HTML, CSS and some knowledge using terminal.
Imported: requests, os, random, load_dotenv and find_dotenv from dotenv, Flask, render_template from flask.
Also, install do npm install -g heroku to install the heroku library.
API used: Spotify, Genius.

I encountered some problems when I was trying to align my text to the center. I also had some problems when I was
trying to fetch the right data and last but not least when my website was not updating the colors and text at all.
Beautifying my website took me quite a while since this is my second time using HTML and CSS.
I also struggled for a little bit since every time my app was refreshed the data wouldn't change. I fixed it by putting
my code into chunks in functions and passing the return from that to an array and passing that when creating the web server
so everytime someone clicks refresh it sends a new request.

I would love to improve my HTML and CSS skill since this could make a simple project like this one
so much nice looking.

You will need to do the following:

1. Create an account at https://developer.spotify.com/ free or premium.
2. Create an account at https://genius.com/api-clients/.
3. Create an App and get the Client ID and Client Secret from Spotify website.
4. Create an App and get the Access Token from the Genius website.
5. Create .env in your directory
    Add lines:

    export ID='YOUR KEY'
    export SECRET='YOUR KEY'
    export GENIUS_ACCESS_TOKEN='YOUR ACCESS TOKEN'

ID is the clientID and SECRET is the client secret from spotify API website developers.
GENIUS_ACCESS_TOKEN is the access token from your app in the Genius API website.

This web app was deployed using Heroku.
