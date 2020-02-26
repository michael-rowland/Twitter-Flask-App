from flask import Blueprint, flash, jsonify, render_template, request
from web_app.models import db, User
from web_app.twitter_service import twitter_api

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    return render_template('index.html')

# @home_routes.route('/users/<screen_name>', methods=["POST"])
# @home_routes.route('/users/<screen_name>')
@home_routes.route('/new_user', methods=['POST'])
def new_user():
    # print('USER:', dict(request.form))

    # user = User(screen_name=request.form['user'])
    # print(user)
    # db.session.add(user)
    # db.session.commit()
    # try:
    screen_name = request.form['screen_name']
    twitter_api_client = twitter_api()

    twitter_user = twitter_api_client.get_user(screen_name)
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()
    
    # flash(f'User "{twitter_user.screen_name} successfully added!', 'test')
    return jsonify({
        'message': 'User successfully added',
        'name': db_user.name,
        'screen_name': db_user.screen_name,
        'location': db_user.location,
        'followers_count': db_user.followers_count
    })


    '''
    twitter_user = twitter_api_client.get_user(screen_name)
    print(twitter_user.id_str)
    print(twitter_user.followers_count)
    # db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user = User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    print(db_user)
    # db.session.add(db_user)
    # db.session.commit()
    # return jsonify(db_user)
    
    # except:
    #     return jsonify({'message': 'user not found'})


    


'''