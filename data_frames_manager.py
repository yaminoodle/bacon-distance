import polars as pl


class DataFramesManager:
    """Manages data-frame queries."""

    def __init__(self, movies_df: pl.DataFrame, actors_df: pl.DataFrame) -> None:
        self.movies_df = movies_df
        self.actors_df = actors_df

    def is_actor_in_data(self, actor_name: str) -> bool:
        actor_name_appearances = self.actors_df.filter(
            pl.col("name") == actor_name
        ).height
        return actor_name_appearances >= 1

    def get_actor_id_by_name(self, actor_name: str) -> str:
        return self.actors_df.filter(pl.col("name") == actor_name).item(0, 0)

    def get_actor_ids_in_movie_by_id(self, movie_id: str) -> pl.Series:
        df = self.movies_df.filter(pl.col("id") == movie_id)

        if df.height > 0:
            return df.item(0, 2)
        return pl.Series()

    def get_movie_ids_of_actor_by_id(self, actor_id: str) -> pl.Series:
        df = self.actors_df.filter(pl.col("id") == actor_id)

        if df.height > 0:
            return df.item(0, 2)
        return pl.Series()
