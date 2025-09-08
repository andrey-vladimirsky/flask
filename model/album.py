from sqlalchemy import PrimaryKeyConstraint

from .. import database


class Album(database.Model):
    __tablename__ = "album"

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(256), nullable=False)
    release_date = database.Column(database.Date, nullable=False)

    # tracks = db.relationship("Track", back_populates="album")

    __table_args__ = (PrimaryKeyConstraint("id", name="pk_album"),)

    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.strftime("%Y-%m-%d"),
        }
