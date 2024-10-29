import json
import requests


class Movie:
    def __init__(self, title, director, year, imdb_code, duration, genres, rating, imdb_score, keywords):
        self.title = title
        self.director = director
        self.year = year
        self.imdb_code = imdb_code
        self.duration = duration
        self.genres = genres
        self.rating = rating
        self.imdb_score = imdb_score
        self.keywords = keywords

    def __repr__(self):
        return f"Title: {self.title}, director: {self.director}, year: {self.year}, IMDB score: {self.imdb_score}"


def search_movie(query):
    url = f"https://movieservice.talkpython.fm/api/search/{query}"
    request = requests.get(url)
    request_j = json.loads(request.text)
    if not request_j["hits"]:
        raise ValueError("No results found")
    for hit in request_j["hits"]:
        yield Movie(**hit)


