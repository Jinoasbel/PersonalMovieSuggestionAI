# https://random-word-api.herokuapp.com/word?number=42 

# Here is your key: 9f5d9eb3

# Please append it to all of your API requests,

# OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=9f5d9eb3

import requests

class ApiManager:

    ApiKey = "9f5d9eb3"
    # SafetyInt = 10

    def RandomWordGenerator(self):

        RndWordApi = "https://random-word-api.herokuapp.com/word?"
        return requests.get(RndWordApi).json()[0]
        
    
    def UpdateList(self):

        # for i in range (0, self.SafetyInt):
            Title = self.RandomWordGenerator()
            OmdbApiUrl = f"http://www.omdbapi.com/?s={Title}&apikey={self.ApiKey}"
            print(OmdbApiUrl)
            return requests.get(OmdbApiUrl).json()


obj = ApiManager()
obj.UpdateList()