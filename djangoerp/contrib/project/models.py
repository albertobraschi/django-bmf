#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from djangoerp.models import ERPModel
from djangoerp.categories import PROJECT
from djangoerp.settings import BASE_MODULE


@python_2_unicode_compatible
class BaseProject(ERPModel):
    if BASE_MODULE["CUSTOMER"]:
        customer = models.ForeignKey(BASE_MODULE["CUSTOMER"], null=True, blank=True, related_name='erp_projects')
    if BASE_MODULE["EMPLOYEE"]:
        employee = models.ForeignKey(BASE_MODULE["EMPLOYEE"], null=True, blank=True)

    name = models.CharField(_("Name"), max_length=255, null=False, blank=False, editable=True, )
    is_bound = models.BooleanField(null=False, blank=True, editable=False, default=False)
    is_active = models.BooleanField(_("Is active"), null=False, blank=True, default=True)

    class Meta: # only needed for abstract models
        verbose_name = _('Project')
        verbose_name_plural = _('Project')
        ordering = ['name']
        abstract = True

    class ERPMeta:
        category = PROJECT

    def __str__(self):
        return self.name

    def erpget_customer(self):
        return self.customer

    def erpget_project(self):
        return self

class AbstractProject(BaseProject):
    """
    """
    notes = models.TextField(null=False, blank=True, )

    class Meta(BaseProject.Meta):
        abstract = True

    class ERPMeta(BaseProject.ERPMeta):
        search_fields = ['name']
        has_logging = True
        has_comments = True
        has_files = True


class Project(AbstractProject):
    pass