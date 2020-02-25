
from flask import Blueprint, jsonify, request, render_template

from web_app.models import db, Tweet, User

tweet_routes = Blueprint("tweet_routes", __name__)


def get_tweets_from_db():
    return [
       {"id": 1, "userid": "111", 'tweet': 'test 1'},
       {"id": 2, "userid": "222", 'tweet': 'test 2'},
       {"id": 3, "userid": "333", 'tweet': 'test 3'},
       {"id": 4, "userid": "444", 'tweet': 'test 4'},
       {"id": 5, "userid": "555", 'tweet': 'test 5'},
       {"id": 6, "userid": "666", 'tweet': 'test 6'},
       ]
    tweets =[]
    tweet_records = Tweet.query.all()
    for t in tweet_records:
        print(t)
        d = t.__dict__
        del d["_sa_instance_state"]
        tweets.append(d)
    return tweets
    

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweets = get_tweets_from_db()
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    tweets = get_tweets_from_db()
    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))

    new_tweet = Tweet(title=request.form["tweet"], userid=request.form["userid"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })
