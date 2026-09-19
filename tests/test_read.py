def test_get_existing_user(client):
    payload = {
            "name": "navid",
            "family": "sadeghi",
            "email": "n@s.com",
            "password": "912345678"
        }
    created = client.post("/users", json=payload). get_json()

    response = client.get(f"/{created["id"]}")

    assert response.status_code == 200
    body =  response.get_json()
    assert body["id"] == created["id"]
    assert body["name"] == "navid"
    assert "password" not in body

def test_get_nonexitent_user_returns_404(client):
    response = client.get("/999")

    assert response.status_code == 404
    assert response.get_json() == {"response": "Client does not exist"}
    