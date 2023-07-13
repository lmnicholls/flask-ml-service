from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Define wait time between tasks
    wait_time = between(1, 5)
    
    @task(1)
    def predicttest(self):
        self.client.post("http://localhost:5000/predict", {
            "CHAS":{
            "0":0
            },
            "RM":{
            "0":6.575
            },
            "TAX":{
            "0":296.0
            },
            "PTRATIO":{
            "0":15.3
            },
            "B":{
            "0":396.9
            },
            "LSTAT":{
            "0":4.98
            }
        })
