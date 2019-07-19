from unittest import TestCase

from app import app


class TestIntegrations(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_survival_endpoint(self):
        response = self.app.get('/api/survival/?name=Hogran John')
        expected_response = {
            "Name": "Horgan, Mr. John",
            "SurvivalChance": 0,
            "Age": None,
            "Embarked": "Q",
            "Parch": 0,
            "Sex": "male",
            "SibSp": 0
        }
        assert response.status_code == 200
        assert response.json == expected_response
        assert type(response.json) == dict
