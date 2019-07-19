import pandas as pd

from prepare_data import (
    encode_embarked,
    encode_sex,
    encode_single_passenger_variables,
    encode_variables,
    encoding_embarked,
    encoding_sex,
    fill_gaps,
    fill_gaps_for_age_column,
    fill_gaps_for_embarked_column,
    fill_single_passenger_gaps
)

training_data = pd.read_csv('data/train.csv')
passenger_mock_dict = {
    'PassengerId': 784,
    'Survived': 0,
    'Pclass': 3,
    'Name': 'Johnston, Mr. Andrew G',
    'Sex': 'male',
    'Age': None,
    'SibSp': 1,
    'Parch': 2,
    'Ticket': 'W./C. 6607',
    'Fare': 23.45,
    'Cabin': None,
    'Embarked': None,
    'LevDist': 3.0000000000000004e-05
}


def test_fill_gaps_for_age_column(df=training_data.copy()):
    assert df['Age'].isna().sum() > 0
    fill_gaps_for_age_column(df)
    assert df['Age'].isna().sum() == 0


def test_fill_gaps_for_embarked_column(df=training_data.copy()):
    assert df['Embarked'].isna().sum() > 0
    fill_gaps_for_embarked_column(df)
    assert df['Embarked'].isna().sum() == 0


def test_encode_sex(df=training_data.copy()):
    assert set(df.Sex.unique()) == set(encoding_sex.keys())
    encode_sex(df)
    assert set(df.Sex.unique()) == set(encoding_sex.values())


def test_encode_embarked(df=training_data.copy()):
    assert set(df[df.Embarked.notnull()].Embarked.unique()) == set(encoding_embarked.keys())
    encode_embarked(df)
    assert set(df[df.Embarked.notnull()].Embarked.unique()) == set(encoding_embarked.values())


def test_all_together_fill_gaps_and_encoding(df=training_data.copy()):
    fill_gaps(df)
    encode_variables(df)
    assert df['Age'].isna().sum() == 0
    assert df['Embarked'].isna().sum() == 0
    assert set(df.Sex.unique()) == set(encoding_sex.values())
    assert set(df.Embarked.unique()) == set(encoding_embarked.values())


def test_fill_single_passenger_gaps():
    passenger = pd.Series(passenger_mock_dict)
    fill_single_passenger_gaps(passenger, training_data)

    assert not passenger.isnull()['Age']
    assert not passenger.isnull()['Embarked']
    assert passenger['Age'] == training_data['Age'].median(skipna=True)
    assert passenger['Embarked'] == training_data['Embarked'].value_counts().idxmax()


def test_encode_single_passenger_variables():
    passenger = pd.Series(passenger_mock_dict)
    raw_data_sex_value = passenger['Sex']
    fill_single_passenger_gaps(passenger, training_data)
    raw_data_embarked_value = passenger['Embarked']
    encode_single_passenger_variables(passenger)
    assert passenger['Sex'] == encoding_sex[raw_data_sex_value]
    assert passenger['Embarked'] == encoding_embarked[raw_data_embarked_value]
