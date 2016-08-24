import random

from django.core.management.base import BaseCommand, CommandError
from jobs.models import Job
from jobs.mixins import JobStatusTransitionMixin

class Command(BaseCommand):
    DEFAULT_NR_JOBS = 10
    
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
    def _job_data(self, **kwargs):
        technology = random.choice(['Java', 'Python', 'Django', 'Javascript', ])
        company_name = random.choice(['Microsoft', 'Yahoo', 'Google', ])

        job = {
            'title': '{} Developer'.format(technology),
            'description': Command._lorem_ipsum(),
            'location': random.choice(['Wien', 'Graz', 'Salzburg']),
            'status': random.choice([
                JobStatusTransitionMixin.STATUS_DRAFT,
                JobStatusTransitionMixin.STATUS_ACTIVE,
                JobStatusTransitionMixin.STATUS_INACTIVE,
            ]),

            'company_name': company_name,
            'external_url': 'http://www.{}.com'.format(company_name.lower()),
            'contact_email': '{}@mailinator.com'.format(company_name.lower()),
        }

        job.update(kwargs)
        return job

    def add_arguments(self, parser):
        self.DEFAULT_NR_JOBS
        parser.add_argument('-i', '--instances',
                            dest='nr_jobs', default=self.DEFAULT_NR_JOBS, 
                            type=int)

    def handle(self, *args, **options):
        for _ in range(options['nr_jobs']):
            job = Job.objects.create(**Command._job_data())
            
            self.stdout.write('\tCreating job ({}).'.format(job))
