import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                credentials[key] = value
    return credentials

if len(sys.argv) > 1:
    username = sys.argv[1]

    # Read credentials from file
    credentials = read_credentials('spotify_credentials.txt')
    
    # Use credentials in SpotifyOAuth
    auth = SpotifyOAuth(scope='user-read-currently-playing',
                        client_id=credentials.get('SPOTIPY_CLIENT_ID'),
                        client_secret=credentials.get('SPOTIPY_CLIENT_SECRET'),
                        redirect_uri=credentials.get('SPOTIPY_REDIRECT_URI'),
                        username=username,
                        open_browser=False)

    token = auth.get_access_token(as_dict=False)

    # Output the token or save it as needed
    print("Access token:", token)

