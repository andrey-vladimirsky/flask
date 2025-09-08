from src.model.album import Album
import src.data.album as data


def list() -> list[Album]:
    return data.list()


def get(id: int) -> Album | None:
    return data.get(id)


def create(album: Album) -> Album:
    return data.create(album)
