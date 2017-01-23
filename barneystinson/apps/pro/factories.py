import factory

from apps.data.factories import IndustryFactory, EmployeeFactory

from .models import Pro


class ProFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pro

    company = factory.Faker('company')
    website = factory.Faker('url')
    description = factory.Faker('text')
    phone = factory.Faker('phone_number')
    industry = factory.SubFactory(IndustryFactory)
    employes = factory.SubFactory(EmployeeFactory)
    ca = 55000
    logo = None
    is_active = True
