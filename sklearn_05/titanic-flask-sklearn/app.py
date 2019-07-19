import pandas as pd
from flask import Flask, request
from sklearn.externals import joblib

from prepare_data import explanatory_vars, pre_process_single_passenger_data
from text import (
    clean_text,
    find_minimum_levenshtein_distance_among_word_permutations,
    get_minimum_levensthein_distance_for_single_word
)

app = Flask(__name__)


def get_prediction_for_passenger(passenger):
    """get classifier prediction for the passenger"""
    passenger_representation = pd.DataFrame(passenger[explanatory_vars].to_dict(), index=[0])
    return classifier.predict(passenger_representation)[0]


def annotate_passenger_with_survival_prediction(passenger):
    preprocessed_passenger = pre_process_single_passenger_data(passenger, passengers)
    passenger['SurvivalChance'] = get_prediction_for_passenger(preprocessed_passenger)


def find_closest_passenger(q_name):
    """performs smart search using Levenshtein distance with following assumption:
    if there is one word of input assume search just by surname, otherwise create all possible
    permutations of search query and find min distance from whole name

    before operations both search term as well as Name are:
     - lowercased,
     - cleaned from stop words,
     - and non-alpha characters
    """
    if len(q_name.split(' ')) == 1:
        passengers['LevDist'] = passengers.apply(
            lambda x: get_minimum_levensthein_distance_for_single_word(text=x['Name'], search_query=q_name),
            axis=1
        )
    else:
        passengers['LevDist'] = passengers.apply(
            lambda x: find_minimum_levenshtein_distance_among_word_permutations(text=x['Name'], search_query=q_name),
            axis=1
        )

    # sort by levensthein distance and pick first (closest in terms of text similarity)
    passengers.sort_values('LevDist', inplace=True)
    return passengers.iloc[0]


@app.route('/api/survival/', methods=['GET'])
def get_passenger():

    serializer_fields = [
        'Name',
        'SurvivalChance',
    ] + explanatory_vars

    closest_passenger = find_closest_passenger(q_name=clean_text(request.args.get('name', '')))
    annotate_passenger_with_survival_prediction(closest_passenger)

    return app.response_class(
        response=closest_passenger[serializer_fields].to_json(),
        status=200,
        mimetype='application/json'
    )


classifier = joblib.load('models/random_forest.pkl')
passengers = pd.read_csv('data/train.csv')

if __name__ == '__main__':
    app.run(debug=True)
