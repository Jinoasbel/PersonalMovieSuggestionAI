import json
import os
from pathlib import Path as path 



class DoesFileExist:
    def __init__(self):
        print("initializing........")
        filea = path("ProcesedMovies.json")
        fileb = path("Watched.json")
        genres = {
        "28": "Action",
        "12": "Adventure",
        "16": "Animation",
        "35": "Comedy",
        "80": "Crime",
        "99": "Documentary",
        "18": "Drama",
        "10751": "Family",
        "14": "Fantasy",
        "36": "History",
        "27": "Horror",
        "10402": "Music",
        "9648": "Mystery",
        "10749": "Romance",
        "878": "Science Fiction",
        "10770": "TV Movie",
        "53": "Thriller",
        "10752": "War",
        "37": "Western"
        }
        
        
        y = {
            "movie":[]
        }
        if not filea.is_file():
            genreX =[0,0,0]
            for genre in genres :
                os.system("cls")                            
                x = input(f"{genres[genre]} -- Do you Like This Genre (Y/N)? ")
                x = x.capitalize()
                match x:
                    case "Y":
                        genreX.append(1)
                    case "N":
                        genreX.append(0)
                    case _:
                        genreX.append(0)

            with open("ProcesedMovies.json","w") as File:
                json.dump({
                        "user_vector":genreX,
                        "genre_list":{"28": "Action",
                        "12": "Adventure",
                        "16": "Animation",
                        "35": "Comedy",
                        "80": "Crime",
                        "99": "Documentary",
                        "18": "Drama",
                        "10751": "Family",
                        "14": "Fantasy",
                        "36": "History",
                        "27": "Horror",
                        "10402": "Music",
                        "9648": "Mystery",
                        "10749": "Romance",
                        "878": "Science Fiction",
                        "10770": "TV Movie",
                        "53": "Thriller",
                        "10752": "War",
                        "37": "Western"},
                        "movies":[]
                    },File,indent=2)
            
        if not fileb.is_file():
            with open("Watched.json", "w") as File:
                json.dump(y,File,indent=2)
        os.system("cls")