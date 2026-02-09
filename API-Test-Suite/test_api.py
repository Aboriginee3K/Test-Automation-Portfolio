import pytest
import requests


class TestReqresAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_single_user(self):
        """
        Test GET request: get user info
        Keypoint: status code return 200, includes 'id' and 'email'
        """

        # 1. send GET request (GET /users/1)
        response = requests.get(f"{self.BASE_URL}/users/1")

        # 2. print the response for debugging
        print(f"GET Response: {response.json()}")

        # 3. Assertion for status code
        assert response.status_code == 200, "Status code should be 200"

        # 4. Assertion json data
        json_data = response.json()
        assert json_data["id"] == 1
        assert "email" in json_data["data"]
        assert "first_name" in json_data["data"]

    def test_create_user(self):
        """
        Test POST request: create a new user
        Keypoint: Status code return 201, includes creation time
        """
        # 1. Payload
        payload = {
            "name": "Yunyi",
            "job": "QA Engineer"
        }

        # 2. send POST request (POST /users)
        response = requests.post(f"{self.BASE_URL}/users", json=payload)

        # 3. print the response for debugging
        print(f"POST Response: {response.json()}")

        # 4. Assertion for status code
        assert response.status_code == 201

        # 5. Assertion for data correctness
        json_data = response.json()
        assert json_data["name"] == "Yunyi"
        assert json_data["job"] == "QA Engineer"
        assert "id" in json_data

    def test_user_not_found(self):
        """
        Test scenario 404: non-exist user
        """
        response = requests.get(f"{self.BASE_URL}/users/9999")
        assert response.status_code == 404