
explained_var = 'Survived'

explanatory_vars = [
    'Age',
    'Embarked',
    'Parch',
    'Sex',
    'SibSp',
]

encoding_sex = {
    'male': 1,
    'female': 0
}

encoding_embarked = {
    'C': 0,
    'Q': 1,
    'S': 2
}


def pre_process_single_passenger_data(passenger, all_passengers):
    # keep original data unmodified by changes (e.g filling the gaps, categories encoding)
    # we need for ai model work
    preprocessed_passenger = passenger.copy()
    # fill gaps
    fill_single_passenger_gaps(preprocessed_passenger, all_passengers)
    # encode categorical variables
    encode_single_passenger_variables(preprocessed_passenger)
    return preprocessed_passenger


def get_median_value_for_gap_in_age(df):
    return df['Age'].median(skipna=True)


def get_mode_value_for_gap_in_embarked(df):
    return df['Embarked'].value_counts().idxmax()


def fill_gaps_for_age_column(df):
    df['Age'].fillna(get_median_value_for_gap_in_age(df), inplace=True)


def fill_gaps_for_embarked_column(df):
    df['Embarked'].fillna(get_mode_value_for_gap_in_embarked(df), inplace=True)


def encode_sex(df):
    df['Sex'] = df.apply(lambda x: encoding_sex.get(x['Sex']), axis=1)


def encode_embarked(df):
    df['Embarked'] = df.apply(lambda x: encoding_embarked.get(x['Embarked']), axis=1)


def fill_single_passenger_gaps(passenger_data, all_passengers):
    if passenger_data.isnull()['Age']:
        passenger_data['Age'] = get_median_value_for_gap_in_age(all_passengers)
    if passenger_data.isnull()['Embarked']:
        passenger_data['Embarked'] = get_mode_value_for_gap_in_embarked(all_passengers)


def fill_gaps(df):
    fill_gaps_for_age_column(df)
    fill_gaps_for_embarked_column(df)


def encode_single_passenger_variables(passenger_data):
    passenger_data['Sex'] = encoding_sex.get(passenger_data['Sex'])
    passenger_data['Embarked'] = encoding_embarked.get(passenger_data['Embarked'])


def encode_variables(df):
    encode_sex(df)
    encode_embarked(df)
