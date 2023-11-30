import spotipy
import requests
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from currentlyPlaying import read_credentials
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
from io import BytesIO

def getCurrentSong():
    # Read credentials from the file
    credentials = read_credentials('spotify_credentials.txt')
    client_id = credentials.get('SPOTIPY_CLIENT_ID')
    client_secret = credentials.get('SPOTIPY_CLIENT_SECRET')
    redirect_uri = credentials.get('SPOTIPY_REDIRECT_URI')
    username = credentials.get('SPOTIPY_USERNAME')

    # Setting up the auth manager with the necessary scope
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope='user-read-currently-playing',
                                username=username)

    # Initializing the Spotipy client with the auth manager
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Fetching the currently playing track and image url
    current_track = sp.current_user_playing_track()
    if current_track is not None and current_track['item'] is not None:
        track = current_track['item']
        track_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        album = track['album']['name']
        
        return{
            'track_name': track_name,
            'artists': artists,
            'album': album,
        }

    else:
        print("No track is currently playing.")
        return None
