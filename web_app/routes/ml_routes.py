from flask import Blueprint, jsonify, render_template, request
from web_app.models import db
from sklearn.linear_model import LogisticRegression

ml_routes = Blueprint('ml_routes', __name__)

@ml_routes.route('/predict', methods=['POST'])
def predict():
    user_1 = request.form['user_1']
    user_2 = request.form['user_2']
    tweet_text = request.form['tweet_text']
    
    # return jsonify({'message':'TODO'})
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)
    return str(clf.predict(X[:2, :]))