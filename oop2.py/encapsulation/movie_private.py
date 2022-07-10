from turtle import title


class Movie:
    def __init__(self,title,year,genre) -> None:
        self._title = title
        self._year = year
        self._genre = genre

    def __get_movie(self):
        print(f'title:{self._title}\ngenre:{self._genre,}')

    def print_detail(self):
        self._get_movie()