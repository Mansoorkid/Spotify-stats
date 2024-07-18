def display_top_tracks(sp):
    results = sp.current_user_top_tracks(limit=10)
    print("Top Tracks:")
    for idx, item in enumerate(results['items']):
        print(f"{idx+1}. {item['name']} by {item['artists'][0]['name']}")

def display_top_artists(sp):
    results = sp.current_user_top_artists(limit=10)
    print("Top Artists:")
    for idx, item in enumerate(results['items']):
        print(f"{idx+1}. {item['name']}")
