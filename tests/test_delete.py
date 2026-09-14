def test_delete_existing_user(client):
    created = client.post(
        "/users"
        json={"name": "navid", "family": "sadeghi", "email": "n@s.com", "password": "x"}
    ).get_json()

    response = client.delete(f"/{created["id"]}")

    assert response.status_code == 200
    assert response.get_json() == {"response": "User deleted successfully"}

    follow_up = client.get(f"/{created["id"]}")
    assert follow_up.status_code == 404


def test_delete_nonexistent_user_returns_404(client):
    response = client.delete("/999")

    assert response.status_code == 404
    assert response.get_json() == {"response": "Client does not exist"}