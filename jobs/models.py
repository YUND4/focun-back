from django.db import models
from django.conf import settings
from common.models import TimestampModel, UUIDModel, StatefulModel

class Company(UUIDModel, TimestampModel, StatefulModel):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Job(UUIDModel, TimestampModel, StatefulModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.ManyToManyField('jobs.Skill')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Application(TimestampModel, StatefulModel):
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job.title}"
