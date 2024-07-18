import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_client
from stats import display_top_tracks, display_top_artists
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    sp = get_spotify_client()
    display_top_tracks(sp)
    display_top_artists(sp)

if __name__ == "__main__":
    main()
