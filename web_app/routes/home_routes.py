from flask import Blueprint, jsonify, render_template, request
from web_app.models import db, User

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    return render_template('index.html')

@home_routes.route('/user', methods=["POST"])
def user_input():
    print('USER:', dict(request.form))

    user = User(user=request.form['user'])
    print(user)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'User successfully added',
        'user': dict(request.form)
    })