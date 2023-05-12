from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main(): # test the root path function named read_main
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_current_quiz():
    response = client.get("/api/current_quiz")
    assert response.status_code == 200
    
    assert response.json()["current_quiz"]["questions"][0]["question"] == "What does the acronym 'UX' stand for?"
    