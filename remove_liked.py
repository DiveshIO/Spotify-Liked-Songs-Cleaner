import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

scope = "user-library-read user-library-modify"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URL"),
    scope=scope
))

results = sp.current_user_saved_tracks(limit = 50)
track_id = []

while results['items']:
    for idx, item in enumerate(results['items']):
        track = item['track']
        track_id.append( track['id'])

    while track_id:
        sp.current_user_saved_tracks_delete(tracks=track_id[:50])
        print(f"Removed songs...")
        track_id = track_id[50:]
    results = sp.current_user_saved_tracks(limit=50, offset=len(track_id))
