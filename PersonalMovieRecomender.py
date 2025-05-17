from DoesFileExist import DoesFileExist 
from ApiManager import ApiManager
from FileManager import FileManager
from PersonalRanking import PersonalRanking
from VectorComputing import VectorComputing
from pathlib import Path as path
import os
import time
import sys
import json

class PersonalMovieRecomender:

        
    DoesFileExist()

    def startup(self):        
        self.filemanager = FileManager()
        self.personalranking = PersonalRanking()


    def main(self):
        
        print("--------------Personal Movie Recomendation--------------")
        self.filemanager.FileWriter()
        print("--------------Ranking Movies Based On your Taste--------------")
        xx = self.personalranking.MovieRanking()
        if not xx:
            print("Something went wrong with the file\nTry to relaunch the application :(")
            time.sleep(5)
            sys.exit()
        if input("Have you Watched any of the Movies(y/s): ").capitalize() == "Y":
            self.personalranking.UpdateUserVector(xx)

        else:
            print("please watch any of the movies")


if __name__ == "__main__":
    x=PersonalMovieRecomender()
    x.startup()
    x.main()
    