from django.conf.urls.defaults import *

urlpatterns = patterns('simple_jobs.views',

   url(
       regex   = '^$',
       view    = 'job_list',
       name    = "job_list",
   ),

    url(
        regex   = '^(?P<job_slug>[\w-]+)/$',
        view    = 'job_detail',
        name    = "job_detail",
    ),

)

