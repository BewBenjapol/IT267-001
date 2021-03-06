from typing_extensions import Self


class Movie:
    def __init__(self) -> None:
        #protected acctrbutes
        self._title = ''
        self._year = 0
        self._genre =''
        self._rating = 6

    #protected method begin with _
    def _add_movie(self,title,year,genre,rating=6):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = rating 

    def _get_movie(self):
        return f'title : {self._title}\nyear : {self._year}\nrating : {self._rating}'