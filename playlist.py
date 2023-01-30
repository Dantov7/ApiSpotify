import requests

class Playlist:
    def __init__(self,base_url,headers,id_playlist):
        self.__base_url = base_url
        self.__headers = headers
        self.__response_playlist=requests.get(self.__base_url+"playlists/"+id_playlist, headers=self.__headers)
                
        self.__total_tracks = len(self.__response_playlist.json()["tracks"]["items"])
        
        params = {
            "ids" : self.__get_ids()
        }

        self.__response_tracks_features=requests.get(self.__base_url+"audio-features/", headers=self.__headers, params=params)

        self.__followers= self.__response_playlist.json()["followers"]["total"]

        self.information = {"Playlist":{"Total_followers":self.__followers,"Features_tracks":self.get_features()}}

        self.__save_image()

    def __get_ids(self):
        
        list_id_tracks=[]

        for number_track in range(self.__total_tracks):
            list_id_tracks.append(self.__response_playlist.json()["tracks"]["items"][number_track]["track"]["id"])

        strings_id = ",".join(list_id_tracks)

        return strings_id

    def get_features (self):
        
        features = ["tempo","acousticness","danceability","energy","instrumentalness","liveness","loudness","valence"]
        list_tempo = []
        list_acousticness = []
        list_danceability = []
        list_energy = []
        list_instrumentalness = []
        list_liveness = []
        list_loudness = []
        list_valence = []

        for i in range(self.__total_tracks):
            for key in features:
                data = self.__response_tracks_features.json()["audio_features"][i][key]
                
                if key == "tempo":
                    list_tempo.append(data)

                elif key == "acousticness":
                    list_acousticness.append(data)

                elif key == "danceability":
                    list_danceability.append(data)                
                
                elif key == "energy":
                    list_energy.append(data)
                
                elif key == "instrumentalness":
                    list_instrumentalness.append(data)
                
                elif key == "liveness":
                    list_liveness.append(data)
                
                elif key == "loudness":
                    list_loudness.append(data)
                
                elif key == "valence":
                    list_valence.append(data)          

        features_tracks = {

            "tempo": self.__get_average(list_tempo),
            "acousticness": self.__get_average(list_acousticness),
            "danceability": self.__get_average(list_danceability),
            "energy": self.__get_average(list_energy),
            "instrumentalness": self.__get_average(list_instrumentalness),
            "liveness": self.__get_average(list_liveness),
            "loudness": self.__get_average(list_loudness),
            "valence": self.__get_average(list_valence)
        }

        return features_tracks
    
    def __get_average(self,list):
        
        suma=0
        for i in list:
            suma += i 
        avergae= suma/len(list)
        return avergae
    
    def __save_image (self):

        response_image=requests.get(self.__response_playlist.json()['images'][0]['url'])

        with open ("image.jpg","wb") as file:
            file.write(response_image.content)
        