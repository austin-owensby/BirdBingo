# Bird Bingo
Bird Bingo game for CAPSHER.

Note that this is intended as light hearted bingo game with minimal features for now.
Currently there is not much protection in place against spamming the server because I'm under the assumption this won't be used maliciously.
If this does not turn out to be the case, I'll attempt to add protections if reasonable, or just remove the site altogether if not.

The production site is deployed here: https://bird-bingo.onrender.com/

## Quick Start
### One Time Setup
1. Install [python](https://www.python.org/downloads/), I developed with `3.12.2`
2. Start a PostgreSQL server.
   - You can either start a [PostgreSQL](https://www.postgresql.org/) server locally
   - OR you can use [Docker](https://www.docker.com/) to run a PostgreSQL server. Ex. `docker run --name local-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:16`
3. Create a PostgreSQL database.
   - Ex. Run `create database bird_bingo` on the PostgreSQL server. 
4. Create an `.env` file at the top directory and add your Postgres database url.
   - Ex. `DATABASE_URL = "DATABASE_URL="postgres://postgres:password@localhost:5432/bird_bingo"`
5. Create a Python virtual environment to keep this project's dependencies separate from your machine's dependencies. You can also do this through VSCode: https://code.visualstudio.com/docs/python/tutorial-flask
   - This should automatically install the python dependencies from the `requirements.txt` and add environmental variables from `.env`
   - If updates are made to the `requirements.txt` you'll need to run `pip install -r requirements.txt` to install the new dependencies.

### Run Project
1. Use VSCode's `Python Debugger: Flask` configuration. This will launch the app with VSCode debugging and open a web browser.
   - If not using VSCode, documentation on how to run and debug python Flask apps are readily available online.

## Database Migrations
Alembic is used to manage the state of the database with migrations.
Migrations will automatically be applied on start up.

To generate a new migration, use: `alembic revision --autogenerate -m "<Migration Name>"`

To manually apply the migration, run `alembic upgrade head`
Or to downgrade, run `alembic downgrade -1` to go back 1 migration, or replace `-1` with a specific revision id.

## Deployment
### One Time Setup
1. Create an account on [Render](https://render.com/)
2. Create a new project
3. Create a new PostgreSQL service on the project.
   - Switch to the Free Tier
   - All other default settings are fine
4. Create a new Web Service service on the project
   - Connect the GitHub repo
   - Update the start command to `gunicorn app.webapp:app`
   - Switch to the Free Tier
   - Create a new environment variable `DATABASE_URL` and copy the environment variable from the PostgreSQL service
   - All other default settings are fine

### Deploy updates
1. Any updates to the `main` branch will cause the code to redeploy
2. Visit https://bird-bingo.onrender.com/ to see the app

## Resources Used
The following is a list of resources I used to set up the app:
- Python Flask project in VSCode with debugging: https://code.visualstudio.com/docs/python/tutorial-flask
- Deployment to Render: https://render.com/
- Postgres ORM, SQL Alchemy: https://www.sqlalchemy.org/
- Postgres Migrations: https://alembic.sqlalchemy.org/en/latest/index.html

## Feature Roadmap
- Update UI with images
- UI Polish (Material library?)
- Handle different screen sizes/devices

### Future Ideas
- Multiple Games (Non-Capsher participants)
- Accounts/Auth
- Source data/images from internet
- Spam protection
- Stress test user inputs
