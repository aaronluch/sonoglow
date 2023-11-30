import spotipy
import requests
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
from io import BytesIO

# Reads the users credentials from file
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                credentials[key] = value
    return credentials

# Downloads and resizes current track image
def download_and_resize_image(url, save_path, size=(32, 32)):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image = image.resize(size)
        image.save(save_path)

# For website image display
def download_and_resize_for_website(url, save_path, size=(512, 512)):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image = image.resize(size)
        image.save(save_path)

def monitor_current_song():
    last_track_id = None
    while True:
        current_track = sp.current_user_playing_track()
        if current_track and current_track['item'] and current_track['item']['id'] != last_track_id:
            track = current_track['item']
            track_name = track['name']
            artists = ", ".join([artist['name'] for artist in track['artists']])
            album = track['album']['name']
            album_cover_art_url = track['album']['images'][0]['url']

            # Download and resize album cover for screen and website
            download_and_resize_image(album_cover_art_url, 'images/currentsong.jpg')
            download_and_resize_for_website(album_cover_art_url, 'static/websitesongdisplay.jpg')

            print(f"You're now listening to '{track_name}' by {artists} from the album '{album}'.")
            last_track_id = current_track['item']['id']

        time.sleep(5)  # Check every 5 seconds
        
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

    # Get the album cover art URL
    album_cover_art_url = track['album']['images'][0]['url']

    # Download and resize album cover for screen
    album_cover_art_url = track['album']['images'][0]['url']
    download_and_resize_image(album_cover_art_url, 'images/currentsong.jpg')

    # Download and resize album cover for website display
    download_and_resize_for_website(album_cover_art_url, 'static/websitesongdisplay.jpg')

    print(f"You're currently listening to '{track_name}' by {artists} from the album '{album}'.")
    print(f"Album cover art URL: {album_cover_art_url}")
    print("Album cover art downloaded and resized.")

else:
    print("No track is currently playing.")