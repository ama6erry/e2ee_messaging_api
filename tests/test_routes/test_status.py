def test_status(client):
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json == {
        "status": "ok"
    }


def test_status_with_name(client):
    response = client.get("/api/status/Name")

    assert response.status_code == 200
    assert response.json == {
        "status": "ok",
        "name": "Name"
    }
