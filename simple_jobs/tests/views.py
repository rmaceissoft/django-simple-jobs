from django.core.urlresolvers import reverse
from django.test import TestCase

from simple_jobs.tests.factories import JobFactory

class JobsViewsTestCase(TestCase):

    def test_job_list(self):
        for i in xrange(3):
            JobFactory()
        resp = self.client.get(reverse('job_list'))
        # Ensure that response contains http code 200
        self.assertEqual(resp.status_code, 200)
        # Ensure that jobs variable is on template context
        self.assertTrue('jobs' in resp.context)

    def test_job_detail(self):
        job = JobFactory()
        resp = self.client.get(reverse('job_detail', kwargs=dict(job_slug=job.slug)))
        # Ensure that response contains http code 200
        self.assertEqual(resp.status_code, 200)
        # Ensure that jobs variable is on template context
        self.assertTrue('job' in resp.context)
        # Ensure that job match with job's slug passed
        self.assertEqual(resp.context['job'], job)

        # Ensure that non-existent jobs throw a 404.
        resp = self.client.get(reverse('job_detail', kwargs=dict(job_slug='foo-bar')))
        self.assertEqual(resp.status_code, 404)


