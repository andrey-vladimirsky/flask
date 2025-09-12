from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint

from src.db import database


class Album(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    band_id = database.Column(database.Integer, nullable=False)
    title = database.Column(database.String(256), nullable=False)
    release_date = database.Column(database.Date, nullable=False)

    __tablename__ = "album"
    # __table_args__ = (
    #     PrimaryKeyConstraint("id", name="pk_album"),
    #     ForeignKeyConstraint(
    #         ["band_id"], ["band.id"], ondelete="CASCADE", name="fk_album_01"
    #     ),
    # )

    # relationship
    # tracks = db.relationship("Track", back_populates="album")

    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.strftime("%Y-%m-%d"),
        }


# CREATE TABLE [dbo].[Album] (
# 	[ID] INTEGER IDENTITY ( 1, 1 ) NOT NULL
# 	, [BandID] INTEGER NOT NULL
# 	, [Title] VARCHAR ( 256 ) NOT NULL
# 	, [ReleaseDate] DATE NOT NULL

# 	, PRIMARY KEY ( [ID] )
# 	, FOREIGN KEY ( [BandID] ) REFERENCES [dbo].[Band] ( [ID] )
# 	, UNIQUE ( [BandID], [Title] )
# )
