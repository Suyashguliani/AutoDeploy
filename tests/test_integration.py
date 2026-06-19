import requests
import time

BASE_URL = "http://localhost:5000"


def test_health():
    for _ in range(10):
        try:
            response = requests.get(f"{BASE_URL}/health")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)

    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"