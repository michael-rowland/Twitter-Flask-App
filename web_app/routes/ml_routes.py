from flask import Blueprint, jsonify, render_template, request
from web_app.models import db
from sklearn.datasets import load_iris

ml_routes = Blueprint('ml_routes', __name__)

@ml_routes.route('/iris')
def iris():
    from sklearn.linear_model import LogisticRegression
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)
    return str(clf.predict(X[:2, :]))

@ml_routes.route('/predict', methods=['POST'])
def predict():
    print('PREDICTING...')
    print('FORM DATA:', dict(request.form))
    return jsonify({'message':'TODO'})