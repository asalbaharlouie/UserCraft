def test_creat_user_success(client):
    payload = {
        "name": "navid",
        "family": "sadeghi",
        "email": "navidsadeghi0021@gmail.com",
        "password": "12345678"
    }

    response = client.pos("/users", json=payload)

    assert response.status_code == 200
    body = response.get_json()
    assert body["id"] == 1
    assert body["name"] == "navid"
    assert body["family"] == "sadeghi"
    assert body["email"] == "navidsadeghi0021@gmail.com"
    assert "password" not in body


def test_creat_user_increments_id(client):
    payload = {"name": "a", "family": "b", "email": "a@b.com", "password": "x"}

    first = client.post("/users", json=payload).get_json()
    second = client.post("/users", json=payload).get_json()

    assert first["id"] == 1
    assert second["id"] == 2

@pytest.mark.parametrize(
    "missing_field",
    ["name", "family", "email", "password"]
)
def test_creat_user_missing_field_return_400(client, misisng_field):
    payload = {
            "name": "navid",
            "family": "sadeghi",
            "email": "navidsadeghi0021@gmail.com",
            "password": "12345678"
    }
    del payload[misisng_field]

    response = client.post("/users, json={}")

    assert response.status_code == 400
    assert response.get_json() == {"response"; "bad request"}

def test_user_empty_body_returns_400(client):
    response = client.post("/users", json={})

    assert response.status_code == 400
    assert response.get_json() == {"response": "bad request"}
    