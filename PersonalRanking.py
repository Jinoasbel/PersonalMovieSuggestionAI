import numpy as np
import json
from pprint import pprint
from sklearn.metrics.pairwise import cosine_similarity

class PersonalRanking:
    
    FileName = "ProcesedMovies.json"
    with open(FileName, 'r') as File:
        Data = json.load(File)

    UserVector = Data.get("user_vector")

    TopRankings = []

    def MovieRanking(self):
        PreferenceVector = []
        self.TopRankings = []

        for movie in self.Data.get("movies"):

            ArrayUser = np.array(self.UserVector)
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
        self.TopRankings = [movie for _, movie in PreferenceVector[:20]]
        pprint(self.TopRankings)
        # print(PreferenceVector)
        return PreferenceVector


    def UpdateUserVector(self, TopRankings):
        
        alpha = 0.1
        suggestion = input("Do you Enjoy the Movie I suggested (Y/N): ").capitalize() 
        if suggestion == "Y" or "YES":
            for Index, movie in enumerate(TopRankings, start = 1):
                    print(f"{Index}-Movie Name :{movie[1].get("name")}")
            IndexName = int(input("Enter The Index of The Movie You Watched : "))
            Movie = TopRankings[IndexName-1]
            self.Data["user_vector"] = [(1 - alpha) * u + alpha * m 
                    for u, m in zip(self.UserVector, Movie[1].get("movie_vector"))
                ]
            print(f"\n\n{self.Data["user_vector"]}")
            with open(self.FileName, 'w') as File:
                json.dump(self.Data, File, indent=4)
        else:
             print("sorry :( can you try Other movie")
             return

            
if __name__ == "__main__":
    obj = PersonalRanking()
    obj.UpdateUserVector(obj.MovieRanking())
