def display_top_tracks(sp):
    results = sp.current_user_top_tracks(limit=10)
    print("\nTop Tracks:")
    for idx, item in enumerate(results['items']):
        print(f"{idx+1}. {item['name']} by {item['artists'][0]['name']}")

def display_top_artists(sp):
    results = sp.current_user_top_artists(limit=10)
    print("\nTop Artists:")
    for idx, item in enumerate(results['items']):
        print(f"{idx+1}. {item['name']}")

def get_top_albums(sp, limit=10):
    # Fetch top tracks
    results = sp.current_user_top_tracks(limit=50)  # You can increase the limit as needed
    albums = {}

    # Collect album information from top tracks
    for item in results['items']:
        album = item['album']
        album_id = album['id']
        if album_id in albums:
            albums[album_id]['count'] += 1
        else:
            albums[album_id] = {
                'name': album['name'],
                'artist': album['artists'][0]['name'],
                'count': 1
            }

    # Sort albums by count and take the top N
    top_albums = sorted(albums.items(), key=lambda x: x[1]['count'], reverse=True)[:limit]

    return top_albums

def display_top_albums(sp, limit=10):
    top_albums = get_top_albums(sp, limit)
    print("\nTop Albums:")
    for idx, (album_id, album) in enumerate(top_albums):
        print(f"{idx+1}. {album['name']} by {album['artist']} (Tracks: {album['count']})")


def display_menu():
    print("\nSpotify Stats Viewer")
    print("1. View Top Tracks")
    print("2. View Top Artists")
    print("3. View Top Albums")
    print("4. View Top Tracks by Genre")
    print("5. Exit")

def get_top_tracks(sp, limit=50):
    results = sp.current_user_top_tracks(limit=limit)
    return results['items']

def get_artist_genres(sp, artist_ids):
    genres = {}
    artists = sp.artists(artist_ids)['artists']
    for artist in artists:
        genres[artist['id']] = artist['genres']
    return genres

def categorize_tracks_by_genre(sp, genre, limit=50):
    top_tracks = get_top_tracks(sp, limit)
    artist_ids = [track['artists'][0]['id'] for track in top_tracks]
    genres = get_artist_genres(sp, artist_ids)

    categorized_tracks = {}
    for track in top_tracks:
        track_name = track['name']
        track_artists = track['artists']
        for artist in track_artists:
            artist_id = artist['id']
            artist_genres = genres.get(artist_id, [])
            if genre in artist_genres:
                if genre not in categorized_tracks:
                    categorized_tracks[genre] = []
                categorized_tracks[genre].append(track_name)

    return categorized_tracks

def display_top_tracks_by_genre(sp, genre, limit=50):
    categorized_tracks = categorize_tracks_by_genre(sp, genre, limit)
    if genre in categorized_tracks:
        print(f"\nTop Tracks in Genre: {genre.capitalize()}")
        for idx, track in enumerate(categorized_tracks[genre]):
            print(f"  {idx + 1}. {track}")
    else:
        print(f"No tracks found for genre: {genre}")