import json

import polars as pl


def generate_db() -> None:
    print("Reading movies...")
    movies_data_frame = pl.read_csv(
        "imdb_api/onek.title.basics.tsv",
        separator="\t",
        null_values="\\N",
        quote_char=None,
        columns=["tconst", "primaryTitle"],
        new_columns=["id", "name"],
    )

    print("Reading actors...")
    actors_data_frame = pl.read_csv(
        "imdb_api/onek.name.basics.tsv",
        separator="\t",
        null_values="\\N",
        quote_char=None,
        columns=["nconst", "primaryName", "knownForTitles"],
        new_columns=["id", "name", "known_for_movies"],
    )

    print("Splitting known_for_movies into a list...")
    actors_data_frame = actors_data_frame.with_columns(
        pl.col("known_for_movies").str.split(by=",")
    )

    print("Calculating actors_in_movies dict...")
    actors_in_movies: dict[str, set[str]] = {}
    for actor in actors_data_frame.iter_rows(named=True):
        if actor["known_for_movies"] == None:
            continue

        for movie in actor["known_for_movies"]:
            actors_in_movies[movie] = actors_in_movies.setdefault(movie, set()) | {
                actor["id"]
            }

    print("Adding actors column to movies_data_frame...")

    def get_actors_in_movie(movie_id) -> list[str]:
        actors_list = list(actors_in_movies.setdefault(movie_id, set()))

        del actors_in_movies[movie_id]

        return actors_list

    movies_data_frame = movies_data_frame.with_columns(
        pl.col("id")
        .map_elements(get_actors_in_movie, return_dtype=pl.List(pl.String))
        .alias("actors")
    )

    print("Writing to output file...")
    with open("db.json", "wt") as db_file:
        db_file.write(
            json.dumps(
                {
                    "movies": movies_data_frame.serialize(format="json"),
                    "actors": actors_data_frame.serialize(format="json"),
                }
            )
        )


def main() -> None:
    generate_db()


if __name__ == "__main__":
    main()
