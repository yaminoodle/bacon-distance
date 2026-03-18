from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bacon_dist_backend.bacon_distance_calculator import BaconDistanceCalculator
from bacon_dist_backend.data_frames_manager import DataFramesManager

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_manager = DataFramesManager("../db.json")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bacon-dist/{actor_name}")
async def calc_bacon_distance(actor_name: str):

    bacon_distance_calculator = BaconDistanceCalculator()
    distance = bacon_distance_calculator.dist_from_actor(actor_name, df_manager)

    return {"bacon_distance": distance.to_eng_string()}