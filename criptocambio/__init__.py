from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()

APIKEY = "E1608E4F-F1D1-4449-B8A4-513461E57ECD"
