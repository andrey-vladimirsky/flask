from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database = SQLAlchemy()
migrate = Migrate()

print("\n", "****************", database, migrate, "****************", "\n", sep="\n")
