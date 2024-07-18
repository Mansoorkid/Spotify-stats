import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_client
from stats import display_top_tracks, display_top_artists, display_menu
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    sp = get_spotify_client()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            display_top_tracks(sp)
        elif choice == '2':
            display_top_artists(sp)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()