from flask import jsonify  # , request
# from sqlalchemy import inspect

from src.db import database
from src.model.album import Album
# from .._model.track import Track


def list() -> list[Album]:
    albums = database.session.query(Album).all()
    response = [album.to_dictionary() for album in albums]
    return jsonify(response)


def get(id) -> Album:
    album = database.session.query(Album).get(id)
    return jsonify(album.to_dictionary())
