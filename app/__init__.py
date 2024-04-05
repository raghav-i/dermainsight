from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='/home/raghav/Documents/Skin-Care/app/static/')
app.config['UPLOAD_PATH'] = '/static/uploads'

from app import routes