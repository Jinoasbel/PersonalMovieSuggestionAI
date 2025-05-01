from ApiManager import ApiManager
from FileManager import FileManager
from PersonalRanking import PersonalRanking
from VectorComputing import VectorComputing

class PersonalMovieRecomender:

    filemanager = FileManager()
    personalranking = PersonalRanking()

    def Main(self):
        print("--------------Personal Movie Recomendation--------------")
        self.filemanager.FileWriter()
        print("--------------Ranking Movies Based On your Taste--------------")
        xx = self.personalranking.MovieRanking()

        if input("Have you Watched any of the Movies(y/s)").capitalize() == "Y":
            self.personalranking.UpdateUserVector(xx)

        else:
            print("please watch any of the movies")


if __name__ == "__main__":
    PersonalMovieRecomender().Main()
    