import random

from django.core.management.base import BaseCommand, CommandError
from jobs.models import Job, Company
from jobs.mixins import JobStatusTransitionMixin


class Command(BaseCommand):
    DEFAULT_NR_JOBS = 10
    COMPANIES = ['Microsoft', 'Yahoo', 'Google', ]

    @classmethod
    def _lorem_ipsum(cls):
        return """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Aenean non lacus ex. Morbi imperdiet nec diam rhoncus finibus.
        Suspendisse pharetra dolor libero, sed egestas massa pellentesque nec.
        Proin convallis et turpis in porta. Cum sociis natoque penatibus et
        magnis dis parturient montes, nascetur ridiculus mus. Morbi vel felis
        lorem. Nam eu urna eget dui semper posuere. Cras libero arcu,
        tincidunt et ipsum sed, lacinia molestie justo. Quisque venenatis arcu
        in leo ullamcorper cursus. In sit amet magna eget lacus aliquam
        fermentum.
        """

    @classmethod
    def _company_data(cls, **kwargs):
        company = {
            'name': random.choice(cls.COMPANIES),
        }
        company.update(kwargs)
        return company

    @classmethod
    def _job_data(cls, company, **kwargs):
        technology = random.choice(['Java', 'Python', 
                                    'Django', 'Javascript', ])

        job = {
            'title': '{} Developer'.format(technology),
            'description': Command._lorem_ipsum(),
            'location': random.choice(['Wien', 'Graz', 'Salzburg']),
            'status': random.choice([
                JobStatusTransitionMixin.STATUS_DRAFT,
                JobStatusTransitionMixin.STATUS_ACTIVE,
                JobStatusTransitionMixin.STATUS_INACTIVE,
            ]),

            'company': company,
            'external_url': 'http://www.{}.com'.format(company.name.lower()),
            'contact_email': '{}@mailinator.com'.format(company.name.lower()),
        }

        job.update(kwargs)
        return job

    def add_arguments(self, parser):
        self.DEFAULT_NR_JOBS
        parser.add_argument('-j', '--jobs',
                            dest='nr_jobs', default=self.DEFAULT_NR_JOBS,
                            type=int)

    def handle(self, *args, **options):
        company_names = list(
            Company.objects.values_list('name', flat=True).distinct()
        )
        for company_name in self.COMPANIES:
            if company_name not in company_names:
                company = Company.objects.create(
                    **Command._company_data(name=company_name))

        companies = Company.objects.all()
        for _ in range(options['nr_jobs']):
            selected_company = random.choice(companies)
            job = Job.objects.create(
                **Command._job_data(company=selected_company))

            self.stdout.write('\tCreating job ({}).'.format(job))
