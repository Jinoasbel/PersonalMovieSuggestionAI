import json
from ApiManager import ApiManager

class FileManager:

    FileName = "ProcesedMovies.json"
    ApiObj = ApiManager()
    SampleData=ApiObj.UpdateList()
    SafetyInt = 10


    def FileWriter(self):
        for i in range (0, self.SafetyInt):
            if self.SampleData.get("Response") is None:
                if self.MovieChecker() == True:
                    with open(self.FileName, "r") as File:
                        data = json.load(File)
                        
                        for movie in self.SampleData.get("Search"):
                            data["movies"].append({
                                "name":movie.get("Title"),
                                "year":movie.get("Year"),
                                "image":movie.get("Poster")
                                })


                            
                    with open(self.FileName, "w") as File:
                        json.dump(data, File, indent=4)
                pass



    def MovieChecker(self):
        return True
        pass

FileManager().FileWriter()

