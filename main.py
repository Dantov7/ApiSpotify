
from auth import Auth
from ranking import Ranking
from playlist import Playlist
from save_jason import save


auth = Auth()

#auth.generate_token()    # use it only for the first time
token = auth.get_token()

base_url = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': f'Bearer {token}',
    "Accept": "application/json"
}

id_playlist= "37i9dQZF1DWWGFQLoP9qlv"

ranking = Ranking(base_url, headers)
playlist = Playlist(base_url, headers,id_playlist)


save(ranking.user_preference, playlist.information)


