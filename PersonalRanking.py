import numpy as np
import json
from pprint import pprint
from sklearn.metrics.pairwise import cosine_similarity

class PersonalRanking:
    
    def __init__(self):
        
        self.FileName = "ProcesedMovies.json"
        with open(self.FileName, 'r') as File:
            self.Data = json.load(File)

        self.UserVector = self.Data.get("user_vector")

        self.TopRankings = []

    def Printer(self):
        for Index, movie in enumerate(self.TopRankings, start = 1):
            print(f"{Index} - Movie Name - {movie.get("name")}")
            print(f"\tReleased On - {movie.get("year")}")
            print(f"\tRating - {movie.get("rating","none")}")

    def MovieRanking(self):
        PreferenceVector = []
        self.TopRankings = []

        for movie in self.Data.get("movies"):

            ArrayUser = np.array(self.UserVector)
            if movie["movie_vector"] == []:
                movie["movie_vector"] = [0,0] 
            ArrayMovie = np.array(movie["movie_vector"])  

            # Clean vectors
            ArrayUser = np.nan_to_num(ArrayUser, nan=0)
            ArrayMovie = np.nan_to_num(ArrayMovie, nan=0)

            # Skip if any vector is all zero
            if np.linalg.norm(ArrayUser) == 0 or np.linalg.norm(ArrayMovie) == 0:
                continue

            # Compute cosine similarity
            Preference = cosine_similarity(ArrayUser.reshape(1, -1), ArrayMovie.reshape(1, -1))[0][0]

            if Preference > 0:
                PreferenceVector.append((Preference, movie))

        # Sort by similarity descending
        PreferenceVector.sort(key=lambda x: x[0], reverse=True)

        # Keep top 20
        with open("Watched.json", "r") as FL:
            Data = json.load(FL)
            x = Data.get("movie")
        
        for _, movie in PreferenceVector:
            if movie.get("name") not in x:
                self.TopRankings.append(movie)

        self.TopRankings = self.TopRankings[:20]
        print(self.TopRankings)
        # pprint(self.TopRankings)
        self.Printer()
        
        # print(PreferenceVector)
        return PreferenceVector


    def UpdateUserVector(self, PreferenceVector):
        
        alpha = 0.1
        if input("Have you watched any of the suggested movies(y/n) : ").capitalize() == "Y":

            suggestion = input("Do you Enjoy the Movie I suggested (Y/N): ").capitalize() 
            if suggestion == "Y" or "YES":
                x=[]
                y = 0
                for Index, movie in enumerate(self.TopRankings, start = 1):
                        print(f"{Index:02} - Movie Name :    {movie.get("name")}")
                        x.append(f"{movie.get("name")}")
                        if Index == 20:
                            break;
                IndexName = int(input("Enter The Index of The Movie You Watched : "))
                y = IndexName-1
                print(self.TopRankings[y].get("name"))
                with open("Watched.json", "r") as F:
                    data = json.load(F) 

                data["movie"].append(x[y])

                with open("Watched.json", "w") as F:
                    json.dump(data, F)

                Movie = PreferenceVector[IndexName-1]
                self.Data["user_vector"] = [(1 - alpha) * u + alpha * m 
                        for u, m in zip(self.UserVector, Movie[1].get("movie_vector"))
                    ]
                print(f"\n\n{self.Data["user_vector"]}")
                with open(self.FileName, 'w') as File:
                    json.dump(self.Data, File, indent=4)
            else:
                print("sorry :( can you try Other movie")
                return
        else:
            print("please Watch Any of the Movies")
            
if __name__ == "__main__":
    obj = PersonalRanking()
    obj.UpdateUserVector(obj.MovieRanking())
