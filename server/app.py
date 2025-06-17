from flask import Flask
from flask_migrate import Migrate
import os

from server.models import db, Customer, Review, Item

app = Flask(__name__, instance_relative_config=True)
db_path = os.path.join(app.instance_path, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)