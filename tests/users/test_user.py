import pytest
import factory
from rest_framework.test import APIClient
from rest_framework import status
from tests.factories import DEFAULT_PASSWORD, AuthenticableFactory

client = APIClient()

@pytest.mark.django_db
def test_create_user(new_user, new_profile, auth_headers):
    new_authentiicable = AuthenticableFactory.build()
    user_data = {
        'email': new_authentiicable.email,
        'password': DEFAULT_PASSWORD,
        'name': new_user.name,
        'last_name': new_user.last_name,
        'description': new_profile.description,
        'country': new_profile.country,
        'phone': new_profile.phone,
    }
    url = '/users/'
    response = client.post(url, user_data, headers=auth_headers)
    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED
