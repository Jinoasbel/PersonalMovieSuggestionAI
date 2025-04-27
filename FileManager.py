import json
from ApiManager import ApiManager

class FileManager:

    def __init__(self):        
        self.FileName = "ProcesedMovies.json"
        ApiObj = ApiManager()
        self.ApiData=ApiObj.UpdateList()
        self.SafetyInt = 10


    def FileWriter(self):
        for i in range (0, self.SafetyInt):

            if (self.ApiData.get("total_results")) != 0:
                print("\n\n\nResponse is True")
                with open(self.FileName, "r") as File:
                    FileData = json.load(File)
                    
                    for movie in self.ApiData.get("results"):

                        if self.MovieChecker(movie.get("original_title")) == True:
                            continue
                        else:
                            print(f"Looping in FileWriter: {movie}")
                            FileData["movies"].append({
                                "name":movie.get("original_title"),
                                "year":movie.get("release_date").split("-")[0],
                                "image_path":movie.get("poster_path"),
                                "genre_ids":movie.get("genre_ids"),
                                "popularity":movie.get("popularity"),
                                "Rating":movie.get("vote_average")

                            })
                            
                            with open(self.FileName, "w") as File:
                                json.dump(FileData, File, indent=4)
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

        return False
                      

FileManager().FileWriter()

