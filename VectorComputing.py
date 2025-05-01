

class VectorComputing:
    
    # GenreVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # Genre = {
    # 28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary',
    # 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music',
    # 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',
    # 10752: 'War', 37: 'Western'
    # }

    Genre_ids = [
    28, 12, 16, 35, 80, 99, 18, 10751,
    14, 36, 27, 10402, 9648, 10749, 878,
    10770, 53, 10752, 37
    ]

    # Others = ["Year", "Rating", "Popularity"]
    # UserPreference = Others+Genre+Actors



    def MovieVector(self, genre):

        GenreVector = [0]*len(self.Genre_ids)
        
        for EachGenre in genre:
            if EachGenre in self.Genre_ids:
                index = self.Genre_ids.index(EachGenre)
                GenreVector[index] = 1
        return GenreVector
        # ArrayOfDict = self.Movies.get("results") # array of dicts

        # for EachDict in ArrayOfDict:  # iterates over each dict in array
        #     print("check")

        #     ArrayOfGenres = EachDict.get("genre_ids") # array of genre values

        # for Index, EachValue in enumerate(self.Genre_ids, start=0): #[0,0,0,0,0,0,0,0,0,0,0,0,0]
        #     print("x")
        #     for EachElement in genre: #[28, 12, 14, 878]
        #         print("y")
        #         if EachValue == EachElement:
        #             #GenreVector.insert(Index, 1)
        #             GenreVector[Index] = 1
        
        # print(GenreVector)
        # return GenreVector
        # # return genrevector


    def min_max_scale(self,value, min_value, max_value):
       # return float(value)*float(min_value)/float(max_value)*float(min_value)
        return abs((value-min_value) / (max_value-min_value))
    

    def Vector2Compute(self, popularity, rating, year):
        Vector2 = [self.min_max_scale(year,1900,2025), self.min_max_scale(rating, 1, 10), abs(popularity/40000)]
        return Vector2
    
    def VectorSummation(self, genre, popularity, rating, year ):
        return self.MovieVector(genre)+self.Vector2Compute(float(popularity), float(rating), float(year))

# print(VectorComputing().VectorSummation())

# "movie_vector":VectorComputing().VectorSummation(movie.get("genre_ids"),
#                                                                                  movie.get("vote_average"),
#                                                                                  movie.get("popularity"),
#                                                                                  movie.get("release_date").split("-")[0]
#                                                                                  )