#!/usr/bin/python3
import os
from typing import List, Tuple
from pprint import pprint
import re


def list_movies() -> List[str]:
    all_movies = []
    movies_path = os.path.join("/media/aminuolawale/TOSHIBA EXT/Movies")
    movie_categories = os.listdir(movies_path)
    for cat in movie_categories:
        category_folder = os.path.join(movies_path, cat)
        movies = [ (*clean_movie_name(a),cat.upper()) for a in os.listdir(category_folder)]
        all_movies.extend(movies)
    return all_movies

def clean_movie_name(movie_name: str)-> Tuple[str, str, str]:
    year = None
    year_search = re.findall("\d{4}", movie_name)
    if year_search and len(year_search) > 0:
        year = year_search[0]
    cleaned_movie_name = movie_name
    if year is not None:
        yi = movie_name.index(year)
        cleaned_movie_name = movie_name[:yi]
    cleaned_movie_name = cleaned_movie_name.strip("() ")
    resolution = None
    res_search = re.findall("\d{3,4}p", movie_name)
    if res_search and len(res_search) > 0:
        resolution = res_search[0]
    return cleaned_movie_name, year, resolution



if __name__ == "__main__":
    result = list_movies()
    # result = clean_movie_name("Bacurau (2019) [1080p] [BluRay] [5.1] [YTS.MX]")
    pprint(result)
