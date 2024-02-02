import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_health_check(auth_headers):
    response = client.get('/health/check/', headers=auth_headers)
    assert response.status_code == 200
    assert response.data == {"status": "OK"}
