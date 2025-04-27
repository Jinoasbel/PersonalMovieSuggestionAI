import json
from ApiManager import ApiManager

class FileManager:

    def __init__(self):        
        self.FileName = "ProcesedMovies.json"
        ApiObj = ApiManager()
        self.SampleData=ApiObj.UpdateList()
        self.SafetyInt = 10


    def FileWriter(self):
        for i in range (0, self.SafetyInt):

            if (self.SampleData.get("Response")) == "True":
                print("\n\n\nResponse is True")
                with open(self.FileName, "r") as File:
                    data = json.load(File)
                    
                    for movie in self.SampleData.get("Search"):

                        if self.MovieChecker(movie.get("Title")) == True:
                            continue
                        else:
                            print(f"Loop in FileWriter: {movie}")
                            data["movies"].append({
                                "name":movie.get("Title"),
                                "year":movie.get("Year"),
                                "image":movie.get("Poster")
                                })
                            
                            with open(self.FileName, "w") as File:
                                json.dump(data, File, indent=4)
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

