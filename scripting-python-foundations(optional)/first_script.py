

from sample_data import favorite_movies, favorite_books


def check_movie_year(movie):
    if movie["release_year"] < 2000:
        print(f'"{movie["title"]}" ({movie["release_year"]}): Released BEFORE 2000.')
    else:
        print(f'"{movie["title"]}" ({movie["release_year"]}): Released AFTER 2000.')
        return movie["title"]


rec_movies = []


# ── HOMEWORK 2, TASK 3: Loop, call the function, conditionally append ──────

print(f'--- Checking release years for the {favorite_movies["name"]} series ---')

for movie in favorite_movies["sequels"]:
    result = check_movie_year(movie)
    if result:
        rec_movies.append(result)


print("\n")
print("Movies released after 2000:")
print(rec_movies)