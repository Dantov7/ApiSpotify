from collections import Counter

import requests
import json


class Ranking:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.endpoint='me/top/'
        params = {

        "limit" : "10",
        "time_range" : "short_term"
        }

        self.response_top10_artist = requests.get(self.base_url+self.endpoint+"artists" , headers=self.headers, params=params)
        self.response_top10_tracks = requests.get(self.base_url+self.endpoint+"tracks" , headers=self.headers, params=params)

        self.list_top_genres=[]
        self.list_top10_artists=[]
        self.list_top10_tracks_with_name_artist=[]

    def __top10_artists(self): 
                
        for i in range(10):
            self.list_top10_artists.append(self.response_top10_artist.json()['items'][i]['name'])
            self.list_top_genres.extend(self.response_top10_artist.json()['items'][i]['genres'])
        return self.list_top10_artists

    def __top5_genres(self):
        
        top_five=[]
        count = Counter(self.list_top_genres)
        for genre in count.most_common(5):
            top_five.append(genre[0])

        return top_five

    def __top10_tracks(self): 
       
        for i in range(10):
            self.list_top10_tracks_with_name_artist.append((self.response_top10_tracks.json()['items'][i]['name'],self.response_top10_tracks.json()['items'][i]['artists'][0]['name']))
        return self.list_top10_tracks_with_name_artist
    

    def save_file(self):

        list_artists=self.__top10_artists()
        list_tracks=self.__top10_tracks()
        list_genres=self.__top5_genres()
        
        with open ("ranking.json","w") as file:

            json.dump({"Top_10_artistas":list_artists, "Top_5_genres":list_genres, "Top_10_tracks": list_tracks}, file)
