from app import app

def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["application"] == "DevOps Lab 4"

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_version():
    client = app.test_client()
    response = client.get("/")
    assert response.get_json()["version"] == "v1"
