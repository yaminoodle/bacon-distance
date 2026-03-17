import json
import io
import polars as pl

from bacon_distance_calculator import BaconDistanceCalculator
from data_frames_manager import DataFramesManager


def load_data_frames() -> DataFramesManager:
    json_db = None

    with open("db.json", "rt") as db_file:
        json_db = json.load(db_file)

    movies_df = pl.DataFrame.deserialize(io.StringIO(json_db["movies"]), format="json")
    actors_df = pl.DataFrame.deserialize(io.StringIO(json_db["actors"]), format="json")

    return DataFramesManager(movies_df, actors_df)


def calc_bacon_dist() -> None:
    actor_name = input("Please enter actor name: ")

    print("Loading data...")
    df_manager = load_data_frames()

    print("Calculating bacon distance...")
    bacon_distance_calculator = BaconDistanceCalculator()
    distance = bacon_distance_calculator.dist_from_actor(actor_name, df_manager)

    print(f"Actor {actor_name}'s bacon distance is: {distance}.")


def main() -> None:
    calc_bacon_dist()


if __name__ == "__main__":
    main()
