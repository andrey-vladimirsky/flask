from flask import Blueprint

from src.model.album import Album
import src.service.album as service

album = Blueprint("album", __name__)


@album.route("/")
def list() -> list[Album]:
    return service.list()


@album.route("/<id>")
def get(id) -> Album:
    return service.get(id)
