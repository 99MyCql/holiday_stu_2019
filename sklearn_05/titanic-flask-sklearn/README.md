# titanic

TASK
----
1.  Download the Titanic training data set for the Titanic prediction challenge from [Kaggle](https://www.kaggle.com/c/titanic/data). (<https://www.kaggle.com/c/titanic/data>)
2.  Build a simple model (of your choice) to predict 'survival' based on 'sex', 'age'. 'sibsp', 'parch' and 'embarked'. **Predictive accuracy of this model won't be judged.**
3.  We now want to deploy this model as a Flask API. The API should take 'Name' as a get parameter and return both the passenger that matches the name most closely as well as the survival prediction for this particular person. Specifically

	1.  Create an endpoint 'survival' which takes 'Name' as a query parameter
	2.  We now want to find the passenger which most closely resembles the name provided in the get-parameter. Which method would you choose to measure how 'close' two names are? Briefly comment on your choice.
	3.  Implement a lookup function that takes as input a name, finds the closest matching passenger in the training data and returns 'sex', 'age','sibsp', 'parch' and 'embarked' for the matched record.
	4.  Predict the chance of survival for that particular passenger using the model you build in 2.
	5.  Let the API return both the matched name as well as the prediction for that name.


HOW TO RUN IT
--------------

OS X install:

	hombrew install python3

using hombrew python and pipenv may cause problems when locale not set, so please export:

	export LANG=en_US.UTF-8
	export LC_ALL=en_US.UTF-8

create pipenv with:

	pipenv --python /usr/local/Cellar/python/3.7.0/bin/python3

activate virtual environment by:

	pipenv shell

install packages by

	pipenv install

web server
==========
run Flask development server by:

	python app.py

and go in web browser to the:

    http://127.0.0.1:5000/api/survival/?name=Horgan
 
Testing
=======

to run this few unit and integration tests, just type in projects directory:

	pytest -v

data science part
=================
lets use well known libraries for doing a bit of data science. Will use [pandas](https://pandas.pydata.org/) for data manipulation, [scikit-learn](http://scikit-learn.org/) for training, and examining our machine learning models, and awesome [jupyter](http://jupyter.org/) notebook for having nice sandbox for all that stuff.

After activating your virtual environment (`pipenv shell`) grab its name and run:

	python -m ipykernel install --user --name={pipven-virtualenv-name-here}

run jupyter notebook if you wish to play a bit machine learning models or just have a look on data:

	jupyter notebook ai_models.ipynb




DISCUSSION
==========

search
------

I picked calculating [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to measure how close two names are.
Because field `Name` contains not only surname, but also first name and title
and this is not exactly said in description what users are going to search by

I decided to come up with following strategy:

(after cleaning stop words like `Mr`, `Mrs`, `Miss`, and `Master` as
causing more chaos than info here and all characters other than a-z + whitespace)

1) if search term is single word, then do search by finding the name with smallest
Levenshtein distance from that word to each of words in field `Name` separately. Assuming the importance of each
consecutive word in `Name` is decreasing, so let's make the levensthein distance even bigger by multiplying it by word position.

2) if search term is more than one word create all possible permutations of it and calculate
the Levenshtein distance to each full Name and pick the minimum from this distances.