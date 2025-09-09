from os import getenv
from flask import Flask

from src.db import database, migrate
from config import configuration
from src.view.album import album

app = Flask(__name__)
app.config.from_object(configuration[getenv("CONFIG_MODE")])

database.init_app(app)
migrate.init_app(app, database)

# print(database, migrate, sep="\n")

app.register_blueprint(album, url_prefix="/album")

if __name__ == "__main__":
    app.run()
