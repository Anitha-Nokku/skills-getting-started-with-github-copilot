from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_manga_maniacs_activity_is_listed_with_expected_details():
    response = client.get("/activities")
    assert response.status_code == 200

    activities = response.json()
    assert "Manga Maniacs" in activities
    assert activities["Manga Maniacs"] == {
        "description": "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        "schedule": "Tuesdays at 7pm",
        "max_participants": 15,
        "participants": [],
    }
