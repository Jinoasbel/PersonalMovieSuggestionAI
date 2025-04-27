# https://random-word-api.herokuapp.com/word?number=42 

# Here is your key: 9f5d9eb3

# Please append it to all of your API requests,

# OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=9f5d9eb3

import requests

class ApiManager:

    ApiKey = "9f5d9eb3"

    def RandomWordGenerator(self):

        RndWordApi = "https://random-word-api.herokuapp.com/word?"
        response = requests.get(RndWordApi).json()[0]
        print(f"RandomWordGenerator: {response}")
        return response

        
    
    def UpdateList(self):

            Title = self.RandomWordGenerator()
            OmdbApiUrl = f"http://www.omdbapi.com/?s={Title}&apikey={self.ApiKey}"
            response = requests.get(OmdbApiUrl).json()
            print(f"UpdateList: {OmdbApiUrl}\nResponse: {response}")

            return response


obj = ApiManager()
obj.UpdateList()