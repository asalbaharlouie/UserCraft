def test_update_user_partial_name_only(client):
    created = client.post(
        "/users"
        json={"name": "navid", "family": "sadeghi", "email": "n@s.com", "password": "x"}
    ).get_json()

    response = client.put("/users", json={"id": created["id"], "name": "reza"})

    assert response.status_code == 200
    body = response.get_json()
    assert body["name"] == "reza"
    assert body["family"] == "sadeghi"
    assert body["email"] == "n@s.com"


def test_update_user_multiple_fields(client):
    created = client.post(
     "/users",
     json={"name": "navid", "family": "baharlouie", "email": "baharlouie@gmail.com", "password": "x"}   
    ).get.json()

    response = client.put("/users", json={"id": created["id"], "family": "baharlouie", "email": "baharlouie@gmail.com"})

    assert response.status_code == 200
    body = response.get_json()
    assert body["name"] == "navid"
    assert body["family"] == "baharlouie"
    assert body["email"] == "baharlouie@gmail.com"


def test_update_nonexistent_user_returns_404(client):
    response = client.put("/users", json={"id": 99, "name": "reza"})

    assert response.status_code == 404
    assert response.get_json() == {"response": "Client does not exist"}


def test_update_without_id_returns_400(client):
    response = client.put("/users", json={"name": "reza"})

    assert response.status_code == 400
    assert response.get_json() == {"response": "bad request"}
    