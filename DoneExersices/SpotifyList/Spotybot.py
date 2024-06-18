from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIFYID = os.getenv("SPOTIFYID")
SPOTIFYSECRET = os.getenv("SPOTIFYSECRET")

if not SPOTIFYID or not SPOTIFYSECRET:
    raise ValueError("Las credenciales de Spotify no están configuradas correctamente en el archivo .env")

billboard = "https://www.billboard.com/charts/hot-100/"
user_input = input("Which year do you want to travel? (format the date in YYYY-MM-DD):\n")
data = requests.get(url=f"{billboard}{user_input}")
soup_billboard = BeautifulSoup(data.text, "html.parser")
song_names_elements = soup_billboard.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_elements]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFYID,
        client_secret=SPOTIFYSECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
playlist_name = f"{user_input} Top 100 Billboard"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(f"Playlist creada: {playlist_name} (ID: {playlist['id']})")

song_uris = []
year = user_input.split("-")[0]

for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        else:
            print(f"{song} no existe en Spotify. Saltado.")
    except Exception as e:
        print(f"Error al buscar la canción {song}: {e}")

if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print("Canciones añadidas a la playlist.")
else:
    print("No se encontraron canciones para añadir a la playlist.")