#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from djangoerp.views import PluginCreate


class EmployeeCreateView(PluginCreate):
    def get_initial(self):
        # TODO: ADD a default product to settings and read the configuration here
#       if self.request.djangoerp_employee:
#          self.initial.update({'product': self.request.erpcore['company'].employee_product_id})
        return super(EmployeeCreateView, self).get_initial()