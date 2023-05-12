from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main(): # test the root path function named read_main
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"},"SPECIFIC ERROR MESSAGE...."

def test_get_current_quiz():
    response = client.get("/api/current_quiz")
    assert response.status_code == 200

    assert response.json()["current_quiz"]["questions"][0]["question"] == "What does the acronym 'UX' stand for?"

def test_user_scores():
    response = client.get("/api/user_scores")
    assert response.status_code == 200

    assert response.json()["user_scores"][0]["name"] == "John Mock4"

def test_user_scores_post():
    response = client.post("/api/user_scores", json={"name": "John Mock4", "score": 4})
    assert response.status_code == 201

    assert response.json()["message"] == "User score created successfully"