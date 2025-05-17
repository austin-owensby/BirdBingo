# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.
from alembic import command
from alembic.config import Config
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    # If developing locally, follow the README to add it
    raise Exception("Could not find a DATABASE_URL environmental variable.")

def run_migrations():
    app.logger.info("Running database migration...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

run_migrations()
