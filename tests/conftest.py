import pytest
from tests.factories import UserFactory, ProfileFactory, AuthenticableFactory, DEFAULT_PASSWORD
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture
def new_user():
    return UserFactory()

@pytest.fixture
def new_profile():
    return ProfileFactory()

@pytest.fixture
def new_authentiicable():
    return AuthenticableFactory()

@pytest.fixture
def auth_token(new_user):
    url = '/auth/'
    response = client.post(url, {'email': new_user.authenticable.email, 'password': DEFAULT_PASSWORD}, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data
    return response.data

@pytest.fixture
def auth_headers(auth_token):
    return {
        'Authorization': f'Bearer {auth_token["access"]}'
    }