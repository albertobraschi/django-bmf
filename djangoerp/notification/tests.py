#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse

from ..testcase import ERPTestCase

class NotificationTests(ERPTestCase):

    def test_notification(self):
        """
        """
        r = self.client.get(reverse('djangoerp:notification'), {})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangoerp:notification'), {'ct': 1})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangoerp:notification'), {'filter': "all"})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangoerp:notification'), {'ct': 1, 'filter': "all"})
        self.assertEqual(r.status_code, 200)