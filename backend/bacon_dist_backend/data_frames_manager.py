import io
import json

import polars as pl


class DataFramesManager:
    """Manages data-frame queries."""

    def __init__(self, db_path: str) -> None:
        json_db = None
        
        with open(db_path, "rt") as db_file:
            json_db = json.load(db_file)

        self.movies_df = pl.DataFrame.deserialize(io.StringIO(json_db["movies"]), format="json")
        self.actors_df = pl.DataFrame.deserialize(io.StringIO(json_db["actors"]), format="json")

    def is_actor_in_data(self, actor_name: str) -> bool:
        actor_name_appearances = self.actors_df.filter( # pyright: ignore[reportUnknownMemberType]
            pl.col("name") == actor_name
        ).height
        return actor_name_appearances >= 1

    def get_actor_id_by_name(self, actor_name: str) -> str:
        return self.actors_df.filter(pl.col("name") == actor_name).item(0, 0) # pyright: ignore[reportUnknownMemberType]

    def get_actor_ids_in_movie_by_id(self, movie_id: str) -> pl.Series:
        df = self.movies_df.filter(pl.col("id") == movie_id) # pyright: ignore[reportUnknownMemberType]

        if df.height > 0:
            return df.item(0, 2)
        return pl.Series()

    def get_movie_ids_of_actor_by_id(self, actor_id: str) -> pl.Series:
        df = self.actors_df.filter(pl.col("id") == actor_id) # pyright: ignore[reportUnknownMemberType]

        if df.height > 0:
            return df.item(0, 2)
        return pl.Series()
