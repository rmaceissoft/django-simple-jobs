import factory

from simple_jobs.models import Job

class JobFactory(factory.Factory):
    FACTORY_FOR = Job

    name = factory.Sequence(lambda n: 'Job Name {0}'.format(n))
    description = factory.Sequence(lambda n: 'Job Description {0}'.format(n))
