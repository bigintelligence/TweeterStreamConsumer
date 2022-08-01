from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_rest_admin_oob():
    response = client.get('/admin/v1/auth/twitter/user/oob')
    assert response.status_code == 200
    assert 'url' in response.json().keys()

