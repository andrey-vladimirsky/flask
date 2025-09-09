from flask import jsonify  # , request
# from sqlalchemy import inspect

from ..db import database
from ..model.album import Album
# from .._model.track import Track


def list():
    albums = database.session.query(Album).all()
    response = [album.to_dictionary() for album in albums]
    return jsonify(response)
