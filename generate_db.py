import json


def generate_db() -> None:
    db_data = {
        "movies": {
            "Apollo 13": {
                "actors": [
                    "Tom Hanks",
                    "Bill Paxton",
                    "Kevin Bacon",
                    "Gary Sinise",
                    "Ed Harris",
                ]
            },
            "The Green Mile": {
                "actors": [
                    "Tom Hanks",
                    "Michael Clarke Duncan",
                    "David Morse",
                    "Bonnie Hunt",
                ]
            },
            "The Truman Show": {"actors": ["Jim Carrey", "Ed Harris", "Laura Linney"]},
        },
        "actors": [
            "Michael Clarke Duncan",
            "David Morse",
            "Bonnie Hunt",
            "Jim Carrey",
            "Gary Sinise",
            "Ed Harris",
            "Laura Linney",
            "Bill Paxton",
            "Tom Hanks",
            "Kevin Bacon",
        ],
    }

    with open("db.json", "wt") as db_file:
        db_file.write(json.dumps(db_data))


def main() -> None:
    generate_db()


if __name__ == "__main__":
    main()
