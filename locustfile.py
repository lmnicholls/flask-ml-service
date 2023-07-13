import time
from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Define wait time between tasks
    wait_time = between(1, 5)
    
    # Test for get endpoint
    @task(1)
    def test1(self):
        self.client.get("http://localhost:5000")
    
    # Test for post endpoint
    @task(2)
    def test2(self):
        self.client.post("http://localhost:5000/predict")
