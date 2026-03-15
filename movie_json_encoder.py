import json

from actor import Actor
from movie import Movie


class MovieJSONEncoder(json.JSONEncoder):
    """Extended json encoder to encode Actor and Movie objects."""

    def default(self, obj) -> str:
        if isinstance(obj, Actor):
            return {
                "name": obj.name,
                "movie_appearance_count": obj.movie_appearance_count,
            }
        elif isinstance(obj, Movie):
            return {"name": obj.name, "starring_actors": obj.starring_actors}

        return super().default(obj)
