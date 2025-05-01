class VectorComputing:

    Genre_ids = [
    28, 12, 16, 35, 80, 99, 18, 10751,
    14, 36, 27, 10402, 9648, 10749, 878,
    10770, 53, 10752, 37
    ]

    def MovieVector(self, genre):

        GenreVector = [0]*len(self.Genre_ids)
        
        for EachGenre in genre:
            if EachGenre in self.Genre_ids:
                index = self.Genre_ids.index(EachGenre)
                GenreVector[index] = 1
        return GenreVector

    def min_max_scale(self,value, min_value, max_value):
        return abs((value-min_value) / (max_value-min_value))
    

    def Vector2Compute(self, popularity, rating, year):
        Vector2 = [self.min_max_scale(year,1900,2025), self.min_max_scale(rating, 1, 10), abs(popularity/40000)]
        return Vector2
    
    def VectorSummation(self, genre, popularity, rating, year ):
        return self.MovieVector(genre)+self.Vector2Compute(float(popularity), float(rating), float(year))
