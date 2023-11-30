# Create or clear the credentials file
credentials_file="spotify_credentials.txt"
> $credentials_file

echo "Enter your Spotify Client ID:"
read spotify_client_id
echo "SPOTIPY_CLIENT_ID=$spotify_client_id" >> $credentials_file

echo "Enter your Spotify Client Secret:"
read spotify_client_secret
echo "SPOTIPY_CLIENT_SECRET=$spotify_client_secret" >> $credentials_file

echo "Enter your Spotify Redirect URI:"
read spotify_redirect_uri
echo "SPOTIPY_REDIRECT_URI=$spotify_redirect_uri" >> $credentials_file

echo "Enter your Spotify username:"
read spotify_username
echo "SPOTIPY_USERNAME=$spotify_username" >> $credentials_file

# Optionally, you can source the file to export the variables to the current session
source $credentials_file

python python/generateToken.py $spotify_username

echo
echo "###### Spotify Token Created ######"
echo "Filename: .cache-$spotify_username"
