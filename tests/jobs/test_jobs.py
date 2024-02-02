import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from tests.factories import JobFactory, SkillFactory, CompanyFactory, Job

@pytest.mark.django_db
def test_list_jobs_without_authentication():
    company = CompanyFactory()
    skill = SkillFactory()
    JobFactory.create_batch(5, company=company, skills=[skill])

    client = APIClient()
    url = '/jobs/'
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5

@pytest.mark.django_db
def test_filter_jobs():
    company = CompanyFactory(name="Tech Company")
    skill = SkillFactory(name="Python")
    JobFactory(title="Developer", company=company, skills=[skill], salary="50000.00")

    client = APIClient()
    url = '/jobs/'

    response = client.get(url, {'company': company.id})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['title'] == "Developer"


@pytest.mark.django_db
def test_job_detail():
    job = JobFactory()

    client = APIClient()
    url = f'/jobs/{job.id}/'
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == str(job.id)  


@pytest.mark.django_db
def test_create_job(auth_headers):
    client = APIClient()
    company = CompanyFactory()
    job_data = {
        "title": "Software Developer",
        "description": "Develop amazing things.",
        "salary": "90000.00",
        "company": company.id
    }
    url = '/jobs/'
    response = client.post(url, job_data, format='json', headers=auth_headers)
    assert response.status_code == status.HTTP_201_CREATED
    assert Job.objects.count() == 1
    job = Job.objects.first()
    assert job.title == job_data["title"]

@pytest.mark.django_db
def test_update_job(auth_headers):
    client = APIClient()
    job = JobFactory()  
    updated_data = {
        "title": "Senior Software Developer",
        "description": "Develop amazing things with more responsibilities.",
        "salary": job.salary,
        "company": job.company.id,
    }
    url = f'/jobs/{job.id}/'
    response = client.put(url, updated_data, format='json', headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    job.refresh_from_db()
    assert job.title == "Senior Software Developer"
    assert job.description == "Develop amazing things with more responsibilities."
