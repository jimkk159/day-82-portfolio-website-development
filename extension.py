from pathlib import Path
import random
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def get_favicon():
    favicon_lists = list(Path('static/icon').iterdir())
    pick_favicon = random.choice(favicon_lists).name
    return pick_favicon
