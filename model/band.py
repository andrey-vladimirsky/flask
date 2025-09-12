import src.model as m


class Band(m.database.Model):
    id = m.database.Column(m.database.Integer, nullable=False)
    name = m.database.Column(m.database.String(256), nullable=False)

    __tablename__ = "band"
    __table_args__ = (
        m.PrimaryKeyConstraint("id", name="pk_band"),
        m.UniqueConstraint("name", name="uq_band_01"),
    )

    # relationship
    # !! to be defined


# CREATE TABLE [dbo].[Band] (
#     [ID] INTEGER IDENTITY ( 1, 1 ) NOT NULL
# 	, [Name] VARCHAR ( 256 ) NOT NULL

# 	, PRIMARY KEY ( [ID] )
# 	, UNIQUE ( [Name] )
# )
