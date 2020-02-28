from flask import Blueprint, jsonify, render_template, request
from sklearn.linear_model import LogisticRegression
from web_app.basilica_service import connection as basilica_client
from web_app.models import db, User, Tweet

ml_routes = Blueprint('ml_routes', __name__)

@ml_routes.route('/predict', methods=['POST'])
def predict():
    screen_name_a = request.form['user_1']
    screen_name_b = request.form['user_2']
    tweet_text = request.form['tweet_text']
    
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = Tweet.query.filter(Tweet.user_id == user_a.id).all()
    user_b_tweets = Tweet.query.filter(Tweet.user_id == user_b.id).all()

    embeddings = []
    labels = []

    for tweet in user_a_tweets:
        labels.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)

    model = LogisticRegression(
        solver='lbfgs',
        multi_class='multinomial')
    model.fit(embeddings, labels)

    pred_embedding = basilica_client.embed_sentence(tweet_text)
    winner = model.predict([pred_embedding])[0]
    loser = screen_name_a if winner == screen_name_b else screen_name_b
    winner_name = User.query.filter(User.screen_name == winner).one().name
    loser_name = User.query.filter(User.screen_name == loser).one().name
    pred_prob = model.predict_proba([pred_embedding])[0]
    pred_pct = pred_prob[0] if pred_prob[0] > pred_prob[1] else pred_prob[1]
    pred_pct = f'{pred_pct*100:.1f}%'
    
    return render_template(
        'prediction.html',
        tweet_text=tweet_text,
        winner=winner_name,
        loser=loser_name,
        prediction_pct=pred_pct
        )