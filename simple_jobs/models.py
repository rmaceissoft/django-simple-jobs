import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug.fields import AutoSlugField

class Job(models.Model):
    slug = AutoSlugField(populate_from='name', unique=True, max_length=255)
    name = models.CharField(verbose_name=_(u'Name'), max_length=255)
    description = models.TextField(verbose_name=_(u'Description'))

    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = _(u'Job')
        verbose_name_plural = _(u'Jobs')

    def __unicode__(self): return self.name

    def save(self, **kwargs):
        self.updated_at = datetime.datetime.now()
        super(Job, self).save(**kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('job_detail', [self.slug])

