import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_auth_url(client_id, client_secret, redirect_uri):
    """
    Generates the Spotify authorization URL.
    """
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope='user-modify-playback-state,user-read-currently-playing',
        open_browser=False
    )
    return auth_manager.get_authorize_url()

def complete_auth(client_id, client_secret, redirect_uri, code):
    """
    Completes the authentication process and retrieves the access token.
    """
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope='user-modify-playback-state,user-read-currently-playing'
    )
    token_info = auth_manager.get_access_token(code)
    return token_info
