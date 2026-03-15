import json

from actor import Actor
from movie import Movie
from movie_json_encoder import MovieJSONEncoder


def generate_db() -> None:
    db_data = {
        "movies": {
            "Apollo 13": Movie(
                "Apollo 13",
                [
                    "Tom Hanks",
                    "Bill Paxton",
                    "Kevin Bacon",
                    "Gary Sinise",
                    "Ed Harris",
                ],
            ),
            "The Green Mile": Movie(
                "The Green Mile",
                [
                    "Tom Hanks",
                    "Michael Clarke Duncan",
                    "David Morse",
                    "Bonnie Hunt",
                ],
            ),
            "The Truman Show": Movie(
                "The Truman Show", ["Jim Carrey", "Ed Harris", "Laura Linney"]
            ),
        },
        "actors": {
            "Michael Clarke Duncan": Actor("Michael Clarke Duncan", 1),
            "David Morse": Actor("David Morse", 1),
            "Bonnie Hunt": Actor("Bonnie Hunt", 1),
            "Jim Carrey": Actor("Jim Carrey", 1),
            "Gary Sinise": Actor("Gary Sinise", 1),
            "Ed Harris": Actor("Ed Harris", 2),
            "Laura Linney": Actor("Laura Linney", 1),
            "Bill Paxton": Actor("Bill Paxton", 1),
            "Tom Hanks": Actor("Tom Hanks", 2),
            "Kevin Bacon": Actor("Kevin Bacon", 1),
        },
    }

    with open("db.json", "wt") as db_file:
        db_file.write(json.dumps(db_data, cls=MovieJSONEncoder))


def main() -> None:
    generate_db()


if __name__ == "__main__":
    main()
