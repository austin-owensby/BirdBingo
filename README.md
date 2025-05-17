# Bird Bingo
Bird Bingo game for CAPSHER.

Note that this is intended as light hearted bingo game with minimal features for now.
Currently there is not much protection in place against spamming the server because I'm under the assumption this won't be used maliciously.
If this does not turn out to be the case, I'll attempt to add protections if reasonable, or just remove the site altogether if not.

## Quick Start
### One Time Setup
1. Install [python](https://www.python.org/downloads/), I developed with `3.12.2`
2. Create a Python virtual environment to keep this project's dependencies separate from your machine's dependencies. You can also do this through VSCode: https://code.visualstudio.com/docs/python/tutorial-flask
3. If not already installed by creating the virtual environment, install python packages with `pip install -r requirements.txt`

### Run Project
1. Use VSCode's `Python Debugger: Flask` configuration. This will launch the app with VSCode debugging and open a web browser.
   - If not using VSCode, documentation on how to run and debug python Flask apps are readily available online.

## Deployment
### One Time Setup
1. Create an account on [Railway](https://railway.com/) and configure access to the repo
2. Create a new component of the Railway architecture from the GitHub repo
3. Go to the setting and choose a setting for Public Networking. I choose to auto generate a domain name.

### Deploy updates
1. Any updates to the `main` branch will cause the code to redeploy
2. Visit https://birdbingo-production.up.railway.app/ to see the app

## Resources used
The following is a list of resources I used to set up the app:
- Python Flask project in VSCode with debugging: https://code.visualstudio.com/docs/python/tutorial-flask
- Deployment to Railway: https://docs.railway.com/guides/flask

## Feature Roadmap
- Connect PostgreSQL Database and deploy
- Storage for board state (Single game)
- Render boards
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
