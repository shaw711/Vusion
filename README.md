# Vusion
## Image analysis using AI 👁

<p align="center">
<img src="logo.png">
</p>

### Installation: (run both client & server simultaneously)
## client:
````bash
cd client

# Install dependencies
npm install

# Start dev server
npm run serve

````

## server:

````bash
cd server
pipenv shell

# Install dependencies (using Pipenv)
sudo pipenv install --skip-lock

# Start server with a category to detect
python server.py
````

### Demo:

<p align="center">
<img src="demo/chameleon.jpg">
<img src="demo/chameleon-results.png">
</p>
<p align="center">
<img src="demo/basketball.jpg">
<img src="demo/basketball-results.png">
</p>


