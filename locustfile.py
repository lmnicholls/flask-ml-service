from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Define wait time between tasks
    wait_time = between(1, 5)
    
    @task
    def predicttest(self):
        self.client.post("https://localhost:5000/predict")
