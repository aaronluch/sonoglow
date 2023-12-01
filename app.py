from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from currentSong import getCurrentSong
import subprocess
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from currentlyPlaying import read_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session

processes = {
    'currentlyPlaying': None,
    'testImage': None,
}

# Read credentials from the file
credentials = read_credentials('spotify_credentials.txt')

client_id = credentials.get('SPOTIPY_CLIENT_ID')
client_secret = credentials.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://localhost:5000/callback'
username = credentials.get('SPOTIPY_USERNAME')

# Add 'user-modify-playback-state' to the scope
scope = 'user-read-currently-playing user-modify-playback-state'

# Setting up the auth manager with the necessary scope
auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope,
                            username=username)

# Initialize Spotify client with the auth manager
sp = spotipy.Spotify(auth_manager=auth_manager)


@app.route('/')
def index():
    song_info = session.get('song_info', {})  # Get song info from session if available
    return render_template('index.html', song_info=song_info)

def run_script(script_name):
    global processes
    if processes[script_name]:
        processes[script_name].terminate()
    processes[script_name] = subprocess.Popen(['python3', f'{script_name}.py'])

@app.route('/updateSong', methods=['POST'])
def currentlyPlaying():
    try:
        run_script('currentlyPlaying')
        message = "currentlyPlaying script executed successfully."
        time.sleep(2) # wait for song to update
        run_script('testImage')
        song_info = getCurrentSong()
        session['song_info'] = song_info  # Store song info in session
        return jsonify(song_info)  # Return song info as JSON
    except subprocess.CalledProcessError as e:
        message = f"An error occurred in currentlyPlaying: {e}"
    return render_template('index.html', message=message, song_info=song_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
