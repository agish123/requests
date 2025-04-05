from locust import HttpUser, task, between

class RequestsUser(HttpUser):
    wait_time = between(0.5, 1)
    
    @task
    def test_get(self):
        self.client.get("/get", headers={"User-Agent": "LoadTest"})