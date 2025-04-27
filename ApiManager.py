# https://random-word-api.herokuapp.com/word?number=42 

# Here is your key: 9f5d9eb3

# Please append it to all of your API requests,

# OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=9f5d9eb3

import requests

class ApiManager:

    ApiKey = "9f5d9eb3"
    TmdbApiKey = "868d76c9b91e24806e8673c3515380e2"

    def RandomWordGenerator(self):

        RndWordApi = "https://random-word-api.herokuapp.com/word?"
        response = requests.get(RndWordApi).json()[0]
        print(f"RandomWordGenerator: {response}")
        return response

        
    
    def UpdateList(self):

            Title = self.RandomWordGenerator()         
            OmdbApiUrl = f"http://www.omdbapi.com/?s={Title}&apikey={self.ApiKey}"
            TmdbApi = f"https://api.themoviedb.org/3/search/movie?api_key={self.TmdbApiKey}&query={Title}"
            response = requests.get(TmdbApi).json()
            print(f"UpdateList: {TmdbApi}\nResponse: {response}")

            return response


obj = ApiManager()
obj.UpdateList()