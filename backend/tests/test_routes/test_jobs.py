import json


def test_create_job(client):
    data = {
        "title": "SD super",
        "company": "dgle",
        "company_url": "www.dgle.com",
        "location": "USA",
        "description": "pyhon",
        "date_posted": "2021-10-11"
        }
    response = client.post("/job/create-job/",json.dumps(data))
    assert response.status_code == 200 
    