import json
import sys

with open("input.txt") as file:
    json_data = file.read().strip()

if not json_data:
    print("file is empty")
    sys.exit(1)

try:
    data = json.loads(json_data)
except json.JSONDecodeError:
    print("incorrect json")
    sys.exit(1)

if not isinstance(data, dict):
    print("incorrect json")
    sys.exit(1)

movies_all = []

for key, movies in data.items():
    if not isinstance(movies, list):
        print("incorrect json")
        sys.exit(1)

    for movie in movies:
        if not isinstance(movie, dict):
            print("incorrect json")
            sys.exit(1)

        if "title" not in movie or "year" not in movie:
            print("incorrect json")
            sys.exit(1)

        movies_all.append(movie)

list0 = {"list0": sorted(movies_all, key=lambda x: x["year"])}

print(json.dumps(list0, indent=4))
