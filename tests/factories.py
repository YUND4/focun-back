import factory
from django.contrib.auth.hashers import make_password
from users.models import Authenticable, User, Profile, Company
from jobs.models import Skill, Job, Application

DEFAULT_PASSWORD = 'testpassword'

class AuthenticableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Authenticable

    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password(DEFAULT_PASSWORD))

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    authenticable = factory.SubFactory(AuthenticableFactory)

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('first_name')
    tax_id = factory.Faker('aba')

    authenticable = factory.SubFactory(AuthenticableFactory)

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    description = factory.Faker('text', max_nb_chars=500)
    country = factory.Faker('country_code')
    phone = factory.Faker('phone_number')

class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    name = factory.Faker('word')

class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job
        skip_postgeneration_save = True

    title = factory.Faker('job')
    description = factory.Faker('paragraph')
    salary = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    company = factory.SubFactory(CompanyFactory) 

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for skill in extracted:
                self.skills.add(skill)

class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    job = factory.SubFactory(JobFactory)
    user = factory.SubFactory(UserFactory)
