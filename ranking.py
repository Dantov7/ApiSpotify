from collections import Counter

import requests

class Ranking:
    def __init__(self, base_url, headers):
        self.__base_url = base_url
        self.__headers = headers
        self.__endpoint='me/top/'
        params = {

        "limit" : "10",
        "time_range" : "short_term"
        }

        self.__response_top10_artist = requests.get(self.__base_url+self.__endpoint+"artists" , headers=self.__headers, params=params)
        self.__response_top10_tracks = requests.get(self.__base_url+self.__endpoint+"tracks" , headers=self.__headers, params=params)

        self.__list_top_genres=[]
        self.__list_top10_artists=[]
        self.__list_top10_tracks_with_name_artist=[]

        self.user_preference = {"User_preference":{"Top_10_artistas":self.__top10_artists(), "Top_5_genres":self.__top5_genres(), "Top_10_tracks": self.__top10_tracks()}}

    def __top10_artists(self): 
                
        for i in range(10):
            self.__list_top10_artists.append(self.__response_top10_artist.json()['items'][i]['name'])
            self.__list_top_genres.extend(self.__response_top10_artist.json()['items'][i]['genres'])
        return self.__list_top10_artists

    def __top5_genres(self):
        
        top_five=[]
        count = Counter(self.__list_top_genres)
        for genre in count.most_common(5):
            top_five.append(genre[0])

        return top_five

    def __top10_tracks(self): 
       
        for i in range(10):
            self.__list_top10_tracks_with_name_artist.append((self.__response_top10_tracks.json()['items'][i]['name'],self.__response_top10_tracks.json()['items'][i]['artists'][0]['name']))
        return self.__list_top10_tracks_with_name_artist
    
