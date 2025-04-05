# locustfile.py
from locust import HttpUser, task, between

class WebUser(HttpUser):
    wait_time = between(1, 5)  # Simulate user wait time between 1 and 5 seconds

    @task
    def fetch_data(self):
        # Simulate a user hitting the /fetch-data endpoint
        self.client.get("/fetch-data")