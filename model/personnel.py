from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint, UniqueConstraint

from src.db import database


class Personnel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    album_id = database.Column(database.Integer, nullable=False)
    participant = database.Column(database.String(256), nullable=False)  ## person id
    description = database.Column(database.String(256), nullable=False)

    __tablename__ = "personnel"
    # __table_args__ = (
    #     PrimaryKeyConstraint("id", name="pk_personnel"),
    #     ForeignKeyConstraint(
    #         ["album_id"], ["album.id"], ondelete="CASCADE", name="fk_personnel_01"
    #     ),
    #     UniqueConstraint("album_id", "participant", name="uq_personnel_01"),
    # )

    # relationship
    # tracks = db.relationship("Track", back_populates="album")

    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
        }


# CREATE TABLE [dbo].[Personnel] (
# 	[ID] INTEGER IDENTITY ( 1, 1 ) NOT NULL
# 	, [AlbumID] INTEGER NOT NULL
# 	, [ArtistID] INTEGER NOT NULL
# 	, [Instrument] VARCHAR ( 128 ) NOT NULL

# 	, PRIMARY KEY ( [ID] )
# 	, FOREIGN KEY ( [AlbumID] ) REFERENCES [dbo].[Album] ( [ID] )
# 	, FOREIGN KEY ( [ArtistID] ) REFERENCES [dbo].[Artist] ( [ID] )

# 	, UNIQUE ( [AlbumID], [ArtistID] )
# )
