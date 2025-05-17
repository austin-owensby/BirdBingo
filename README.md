# Bird Bingo
Bird Bingo game for CAPSHER.

Note that this is intended as light hearted bingo game with minimal features for now.
Currently there is not much protection in place against spamming the server because I'm under the assumption this won't be used maliciously.
If this does not turn out to be the case, I'll attempt to add protections if reasonable, or just remove the site altogether if not.

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
1. Create an account on [Railway](https://railway.com/) and configure access to the repo
2. Create a new component of the Railway architecture from the GitHub repo
3. Go to the setting and choose a setting for Public Networking. I choose to auto generate a domain name.
4. Create a PostgreSQL Database component
5. On the GitHub component, add a new environment variable DATABASE_URL and reference the variable from the PostgreSQL component
6. I choose to turn on serverless to ideally lower costs

### Deploy updates
1. Any updates to the `main` branch will cause the code to redeploy
2. Visit https://birdbingo-production.up.railway.app/ to see the app

## Resources Used
The following is a list of resources I used to set up the app:
- Python Flask project in VSCode with debugging: https://code.visualstudio.com/docs/python/tutorial-flask
- Deployment to Railway: https://docs.railway.com/guides/flask
- PostgreSQL Database deployment to Railway: https://docs.railway.com/guides/build-a-database-service
- Postgres ORM, SQL Alchemy: https://www.sqlalchemy.org/
- Postgres Migrations: https://alembic.sqlalchemy.org/en/latest/index.html

## Feature Roadmap
- Update boards on card draw
- Win state
- Start new game
- Poll for updates to keep users in sync
- Update UI with images
- Ask for name
- Storage for turn log
- Record and display user logs
- Storage for win statistics
- Update and display win statistics
- Disclaimer about data usage and storage
- UI Polish (Material library)
- Handle different screen sizes/devices

### Future Ideas
- Multiple Games (Non-Capsher participants)
- Accounts/Auth
- Source data/images from internet
- Spam protection
- Stress test user inputs
