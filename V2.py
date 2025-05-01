import os
import json
from ApiManager import ApiManager
from VectorComputing import VectorComputing

class FileManager:
    def __init__(self):
        self.FileName = "ProcesedMovies.json"
        self.SafetyInt = 1
        self.EnsureFileExists()
        self.ApiData = ApiManager().UpdateList()

    def EnsureFileExists(self):
        if not os.path.exists(self.FileName):
            with open(self.FileName, "w") as f:
                json.dump({"movies": []}, f, indent=4)

    def FileWriter(self):
        if not self.ApiData or self.ApiData.get("total_results") == 0:
            print("No results to process.")
            return

        with open(self.FileName, "r") as f:
            FileData = json.load(f)

        for movie in self.ApiData.get("results", []):
            movie_name = movie.get("original_title")
            if self.MovieChecker(movie_name):
                continue

            release_date = movie.get("release_date", "")
            year = release_date.split("-")[0] if release_date else "Unknown"

            print(f"Adding movie: {movie_name}")
            FileData["movies"].append({
                "name": movie_name,
                "year": year,
                "image_path": movie.get("poster_path"),
                "genre_ids": movie.get("genre_ids"),
                "popularity": movie.get("popularity"),
                "Rating": movie.get("vote_average"),
                "movie_vector": VectorComputing().VectorSummation(
                    genre=movie.get("genre_ids"),
                    rating=movie.get("vote_average"),
                    popularity=movie.get("vote_count"),  # clarify this name
                    year=year
                )
            })

        with open(self.FileName, "w") as f:
            json.dump(FileData, f, indent=4)

    def MovieChecker(self, Movie):
        with open(self.FileName, "r") as f:
            Data = json.load(f)
        return any(MovieName.get("name") == Movie for MovieName in Data.get("movies", []))

# Run it
FileManager().FileWriter()
