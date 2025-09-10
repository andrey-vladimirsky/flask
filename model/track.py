from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint, UniqueConstraint

from ..db import database


class Track(database.Model):
    __tablename__ = "track"

    id = database.Column(database.Integer, nullable=False)
    album_id = database.Column(database.Integer, nullable=False)

    orderno = database.Column(database.Integer, nullable=False)
    title = database.Column(database.String(256), nullable=False)
    duration = database.Column(database.Integer, nullable=False)

    # relationship
    # album = database.relationship("Album", back_populates="tracks")

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_track"),
        ForeignKeyConstraint(
            ["album_id"], ["album.id"], ondelete="CASCADE", name="fk_track_01"
        ),
        UniqueConstraint("album_id", "orderno", name="uq_track_01"),
    )

    def str_to_duration(s):
        return sum(
            map(
                lambda x, y: x * y,
                [int(time_part) for time_part in s.split(":")],
                [3600, 60, 1],
            )
        )
