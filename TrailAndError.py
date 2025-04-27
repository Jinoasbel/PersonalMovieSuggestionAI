import json
FileName = "ProcesedMovies.json"


def MovieChecker():

  print("\n\n\nMovieChecker")
  with open(FileName, "r") as File:
    Data = json.load(File)
  for MovieName in Data.get("movies"): 
    print(MovieName.get("name"))

MovieChecker()