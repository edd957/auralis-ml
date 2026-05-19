from fastapi.testclient import TestClient

from auralis_ml.api.app import create_app


def test_chat_ingest_and_energy_endpoint() -> None:
    client = TestClient(create_app())

    response = client.post(
        "/chat",
        json={"author": "viewer", "message": "this is fire, go faster", "platform": "demo"},
    )
    assert response.status_code == 200

    energy = client.get("/energy")
    assert energy.status_code == 200
    assert energy.json()["message_count"] == 1
