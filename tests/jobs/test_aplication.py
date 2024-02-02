import pytest
from rest_framework.test import APIClient
from rest_framework import status
from tests.factories import JobFactory
from jobs.models import Application

client = APIClient()

@pytest.mark.django_db
def test_application_creation(auth_headers):
    job = JobFactory()

    application_data = {
        "job": job.id,
    }

    url = '/applications/'
    response = client.post(url, application_data, format='json', headers=auth_headers)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['job'] == job.id


    applications = Application.objects.all()
    assert applications.count() == 1
    application = applications.first()
    assert application.job == job
