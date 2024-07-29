import spotipy
from spotipy.oauth2 import SpotifyOAuth

def do_authorize(client_id: str, client_secret: str):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri="http://localhost:8080/callback",
                                                scope="playlist-modify-public")) #playlist-modify-public, user-library-read
    return sp

def list_songs_by_name(sp, name: str):
    results = sp.search(q=name, limit=10)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

    return results['tracks']['items']

def add_song_to_playlist(sp, song_id: str, playlist_id: str):
    track_uris = [f'spotify:track:{song_id}']
    sp.playlist_add_items(playlist_id, track_uris)