from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Customer, Item, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


@app.route('/customers')
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])


@app.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify([i.to_dict() for i in items])


@app.route('/reviews')
def get_reviews():
    reviews = Review.query.all()
    return jsonify([r.to_dict() for r in reviews])


if __name__ == '__main__':
    app.run(port=5555, debug=True)
