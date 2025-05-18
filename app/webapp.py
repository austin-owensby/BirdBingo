# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from .controllers import views  # Import side-effects of setting up views.
from .controllers import requests  # Import side-effects of setting up requests.
from alembic import command
from alembic.config import Config

def run_migrations():
    app.logger.info("Running database migration...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

run_migrations()
