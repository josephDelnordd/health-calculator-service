import unittest
import json
from app import app
from health_utils import calculate_bmi, calculate_bmr


class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr_male(self):
        self.assertAlmostEqual(
            calculate_bmr(175, 70, 25, "male"), 1724.05, places=2
        )


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_bmi_endpoint(self):
        response = self.client.post(
            "/bmi",
            data=json.dumps({"height": 1.75, "weight": 70}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_bmr_endpoint(self):
        response = self.client.post(
            "/bmr",
            data=json.dumps({
                "height": 175,
                "weight": 70,
                "age": 25,
                "gender": "male"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()