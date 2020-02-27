from flask import Blueprint, flash, jsonify, render_template, redirect, request
from web_app.models import db, User, Tweet
from web_app.twitter_service import twitter_api
from web_app.basilica_service import connection as basilica_client

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@home_routes.route('/new_user', methods=['POST'])
def new_user():

    try:
        screen_name = request.form['screen_name']
        twitter_api_client = twitter_api()

        twitter_user = twitter_api_client.get_user(screen_name)
        db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
        db_user.screen_name = twitter_user.screen_name.lower()
        db_user.name = twitter_user.name
        db_user.location = twitter_user.location
        db_user.followers_count = twitter_user.followers_count
        db_user.profile = twitter_user.profile_image_url_https
        db.session.add(db_user)
        db.session.commit()
        
        statuses = twitter_api_client.user_timeline(
            screen_name, 
            tweet_mode="extended", 
            count=50, 
            exclude_replies=True, 
            include_rts=False)
        statuses_full_text = [status.full_text for status in statuses]

        embeddings = basilica_client.embed_sentences(
            statuses_full_text,
            model='twitter')
        embeddings_list = [embedding for embedding in embeddings]

        counter = 0
        for status in statuses:
            db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
            db_tweet.user_id = status.author.id
            db_tweet.full_text = status.full_text
            db_tweet.embedding = embeddings_list[counter]
            db.session.add(db_tweet)
            counter += 1
        db.session.commit()

        flash(f'User "{twitter_user.name}" successfully added!')
        return redirect('/')
 
    except:
        return redirect('/user_not_found')

# ********************
# DELETE THIS
# ********************
@home_routes.route('/users')
def all_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@home_routes.route('/user_not_found')
def user_not_found():
    return render_template('user_not_found.html')

@home_routes.route('/user/<screen_name>')
def user(screen_name=None):
    # try
    user = User.query.filter_by(screen_name=screen_name).first()
    tweets = Tweet.query.filter_by(user_id=user.id).all()
    return render_template('user.html', user=user, tweets=tweets)