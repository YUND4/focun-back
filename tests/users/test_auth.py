import pytest
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_token_obtain_pair(auth_token):
    pass

@pytest.mark.django_db
def test_token_refresh(auth_token):
    url = '/auth/refresh/'
    refresh_token = auth_token['refresh']
    response = client.post(url, {'refresh': refresh_token}, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data

@pytest.mark.django_db
def test_token_verify(auth_token):
    url = '/auth/verify/'
    access_token = auth_token['access']
    response = client.post(url, {'token': access_token}, format='json')
    assert response.status_code == status.HTTP_200_OK
