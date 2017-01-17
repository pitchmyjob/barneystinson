from django.core.management.base import BaseCommand, CommandError

from apps.data.models import Industry, Employee, ContractType, Experience, StudyLevel
from ._data import INDUSTRIES, EMPLOYEES, CONTRACT_TYPES, EXPERIENCES, STUDY_LEVELS


class Command(BaseCommand):
    help = 'Initializes the database with basic data'

    industries = INDUSTRIES
    employees = EMPLOYEES
    contract_types = CONTRACT_TYPES
    experiences = EXPERIENCES
    study_levels = STUDY_LEVELS

    def handle(self, *args, **options):
        self.stdout.write('# init_data command start')
        self.add_general_data(Industry, 'industries')
        self.add_general_data(Employee, 'employees')
        self.add_general_data(ContractType, 'contract_types')
        self.add_general_data(Experience, 'experiences')
        self.add_general_data(StudyLevel, 'study_levels')
        self.stdout.write('\n# init_data command end')

    def add_general_data(self, model, var_name):
        self.stdout.write('\n>> Add "{}" data'.format(model.__name__))

        names = getattr(self, var_name, None)
        if names:
            order = 10
            for name in names:
                obj, created = model.objects.get_or_create(name=name, defaults={'order': order})
                if created:
                    self.stdout.write(self.style.SUCCESS('"{}" has been created with order {} and id {}'.format(name, order, obj.pk)))
                else:
                    self.stdout.write(self.style.WARNING('"{}" already exists with order {} and id {}'.format(name, obj.order, obj.pk)))
                order += 10
        else:
            self.stderr.write('No data to deal with')
