from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Define wait time between tasks
    wait_time = between(1, 5)
    
    # Test for get endpoint
    @task(1)
    def test1(self):
        self.client.get("http://localhost:5000")

    @task(2)
    def test2(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }
        
        payload = {
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
        }
        
        self.client.post("http://localhost:5000/predict", data=payload, headers=headers)
