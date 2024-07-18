# Importing modules to make them available at the package level
from .auth import get_spotify_client
from .stats import display_top_tracks, display_top_artists
from .utils import *  # If you have any utility functions to expose
