def test_tasks_page(client):
    response = client.get("/tasks")
    assert response.status_code in (200, 302)
