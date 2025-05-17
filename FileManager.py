import json
from ApiManager import ApiManager
from VectorComputing import VectorComputing
import os

class FileManager:

    def __init__(self):        
        self.FileName = "ProcesedMovies.json"
        ApiObj = ApiManager()
        self.ApiData=ApiObj.UpdateList()
        self.SafetyInt = 1


    def FileWriter(self):
        
        with open(self.FileName, "r") as File:
            FileData = json.load(File)
            for i in range (0, self.SafetyInt):
                os.system("cls")
                if self.ApiData and self.ApiData.get("total_results") != 0:
                    print("\n\n\nResponse is True")    
                    for movie in self.ApiData.get("results"):

                        if self.MovieChecker(movie.get("original_title")) == True:
                            continue
                        else:
                            print(f"\n\n\n\n\nLooping in FileWriter: {movie}")
                            FileData["movies"].append({
                                "name":movie.get("original_title"),
                                "year":movie.get("release_date").split("-")[0],
                                "image_path":movie.get("poster_path"),
                                "genre_ids":movie.get("genre_ids"),
                                "popularity":movie.get("popularity"),
                                "Rating":movie.get("vote_average"),
                                "movie_vector":VectorComputing().VectorSummation(genre = movie.get("genre_ids"),
                                                                                rating = movie.get("vote_average"),
                                                                                popularity = movie.get("vote_count"),
                                                                                year = movie.get("release_date").split("-")[0] if movie.get("release_date") else "2000"
                                                                                )

                            }
                            )
                                
                            with open(self.FileName, "w") as File:
                                json.dump(FileData, File, indent = 2)
                else:
                    continue


    def MovieChecker(self, Movie):

        print("\n\n\nMovieChecker")
        with open(self.FileName, "r") as File:
            Data = json.load(File)
        for MovieName in Data.get("movies"): 

            print(f"{MovieName.get("name")} : {Movie}")
            if MovieName.get("name") == Movie:
                return True
            else:
                continue
        os.system("cls")
        return False
                      
if __name__ == "__main__":
    x = FileManager()
    x.FileWriter()

