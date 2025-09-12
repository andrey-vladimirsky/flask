from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint, UniqueConstraint

from src.db import database


class Track(database.Model):
    id = database.Column(database.Integer, nullable=False)
    album_id = database.Column(database.Integer, nullable=False)
    ordinal_no = database.Column(database.Integer, nullable=False)
    title = database.Column(database.String(256), nullable=False)
    duration = database.Column(database.Integer, nullable=False)

    __tablename__ = "track"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_track"),
        ForeignKeyConstraint(
            ["album_id"], ["album.id"], ondelete="CASCADE", name="fk_track_01"
        ),
        UniqueConstraint("album_id", "ordinal_no", name="uq_track_01"),
    )

    # relationship
    # album = database.relationship("Album", back_populates="tracks")

    def str_to_duration(s):
        return sum(
            map(
                lambda x, y: x * y,
                [int(time_part) for time_part in s.split(":")],
                [3600, 60, 1],
            )
        )


# CREATE TABLE [dbo].[Track] (
# 	[ID] INTEGER IDENTITY ( 1, 1 ) NOT NULL
# 	, [AlbumID] INTEGER NOT NULL
# 	, [No] INTEGER NOT NULL -- ordinal
# 	, [Title] VARCHAR ( 256 ) NOT NULL
# 	, [Duration] INTEGER NOT NULL

# 	, PRIMARY KEY ( [ID] )
# 	, FOREIGN KEY ( [AlbumID] ) REFERENCES [dbo].[Album] ( [ID] )
# 	, UNIQUE ( [AlbumID], [No] )
# 	, UNIQUE ( [AlbumID], [Title] )
# )
