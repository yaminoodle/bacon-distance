from bacon_distance_calculator import BaconDistanceCalculator
from data_frames_manager import DataFramesManager


def calc_bacon_dist() -> None:
    actor_name = input("Please enter actor name: ")

    print("Loading data...")
    df_manager = DataFramesManager("../db.json")

    print("Calculating bacon distance...")
    bacon_distance_calculator = BaconDistanceCalculator()
    distance = bacon_distance_calculator.dist_from_actor(actor_name, df_manager)

    print(f"Actor {actor_name}'s bacon distance is: {distance}.")


def main() -> None:
    calc_bacon_dist()


if __name__ == "__main__":
    main()
