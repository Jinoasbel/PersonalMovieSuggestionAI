

class VectorComputing:
    
    Actors = [
    "Robert Downey Jr.",
    "Leonardo DiCaprio",
    "Tom Cruise",
    "Johnny Depp",
    "Brad Pitt",
    "Dwayne Johnson",
    "Ryan Reynolds",
    "Chris Hemsworth",
    "Tom Holland",
    "Pedro Pascal"
]

    GenreVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Genre = {
    28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary',
    18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music',
    9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',
    10752: 'War', 37: 'Western'
    }



    Others = ["Year", "Rating", "Popularity"]
    UserPreference = Others+Genre+Actors


    Movies = {
        "page": 1,
        "results": [
        {
            "adult": False,
            "backdrop_path": "/vL5LR6WdxWPjLPFRLe133jXWsh5.jpg",
            "genre_ids": [28, 12, 14, 878],
            "id": 19995,
            "original_language": "en",
            "original_title": "Avatar",
            "overview": "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.",
            "popularity": 26.1186,
            "poster_path": "/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
            "release_date": "2009-12-15",
            "title": "Avatar",
            "video": False,
            "vote_average": 7.589,
            "vote_count": 32179
        },
        {
            "adult": False,
            "backdrop_path": None,
            "genre_ids": [18],
            "id": 1096978,
            "original_language": "es",
            "original_title": "Avatar",
            "overview": "Tension mounts between a quadraplegic man and his wife as she prepares a bath for him.",
            "popularity": 0.4912,
            "poster_path": "/gmnD2e1RvMdCl9D1rsDEQaQlJxK.jpg",
            "release_date": "2006-04-11",
            "title": "Avatar",
            "video": False,
            "vote_average": 5.941,
            "vote_count": 59
        }
        ],
        "total_pages": 4,
        "total_results": 79
    }



    def MovieVector(self):

        ArrayOfDict = self.Movies.get("results") # array of dicts

        for EachDict in ArrayOfDict:  # iterates over each dict in array

            ArrayOfGenres = EachDict.get("genre_ids") # array of genre values

            for Index, EachValue in enumerate(self.Genre_ids, start=0):
                for EachElement in ArrayOfGenres:
                    if EachValue == EachElement:
                        self.GenreVector.insert(Index, 1)
        
        print(self.GenreVector)
        return self.GenreVector


    def min_max_scale(value, min_value, max_value):
        return (value - min_value) / (max_value - min_value)

print(VectorComputing().MovieVector())