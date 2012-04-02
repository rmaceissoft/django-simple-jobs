from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from simple_jobs.models import Job


def job_list(request, template_name="simple_jobs/job_list.html"):
    context = dict(
        jobs = Job.objects.all()
    )
    return TemplateResponse(request, template_name, context)


def job_detail(request, job_slug, template_name="simple_jobs/job_detail.html"):
    context = dict(
        job = get_object_or_404(Job, slug=job_slug)
    )
    return TemplateResponse(request, template_name, context)

