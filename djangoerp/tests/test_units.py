#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from django.test import TestCase

from django.core.exceptions import ImproperlyConfigured
from django.core.exceptions import ValidationError
from django.utils import six
from django.utils.translation import activate

from django.utils.translation import ugettext_lazy as _

from ..currency import BaseCurrency

from decimal import Decimal


class ClassTests(TestCase):
    def test_currency(self):
        activate('en')

#   msg = "missing iso"
#   with self.assertRaises(ImproperlyConfigured, msg=msg):
#     class TestCurrency(BaseCurrency):
#       name = 'Currency'
#       symbol = 'c'

#   msg = "missing name"
#   with self.assertRaises(ImproperlyConfigured, msg=msg):
#     class TestCurrency(BaseCurrency):
#       iso = "XTE"
#       symbol = 'c'

#   msg = "missing symbol"
#   with self.assertRaises(ImproperlyConfigured, msg=msg):
#     class TestCurrency(BaseCurrency):
#       iso = "XTE"
#       name = 'Currency'

#   msg = "invalid precision (A)"
#   with self.assertRaises(ImproperlyConfigured, msg=msg):
#     class TestCurrency(BaseCurrency):
#       iso = "XTE"
#       name = 'Currency'
#       symbol = 'c'
#       precision = 'invalid'

#   msg = "invalid precision (B)"
#   with self.assertRaises(ImproperlyConfigured, msg=msg):
#     class TestCurrency(BaseCurrency):
#       iso = "XTE"
#       name = 'Currency'
#       symbol = 'c'
#       precision = -3

#   # valid models
#   class TestCurrency(BaseCurrency):
#     iso = "XTE"
#     name = 'Currency'
#     symbol = 'c'
#     symbol = six.u('¢') # LOOK test unicode-characters
#     precision = 3

#   class DemoCurrency(BaseCurrency):
#     iso = "XDL"
#     name = 'Dollar'
#     symbol = '$'
#     symbol = _('ł') # LOOK test translations
#     precision = 2

#   # logic

#   self.assertTrue(TestCurrency(1))

#   self.assertTrue(TestCurrency(1) == TestCurrency(1))
#   self.assertTrue(TestCurrency(1) != TestCurrency(2))

#   self.assertTrue(TestCurrency(1) >= TestCurrency(1))
#   self.assertTrue(TestCurrency(2) >  TestCurrency(1))
#   self.assertTrue(TestCurrency(1) <= TestCurrency(1))
#   self.assertTrue(TestCurrency(1) <  TestCurrency(2))

#   self.assertFalse(TestCurrency(1) == DemoCurrency(1))
#   self.assertFalse(TestCurrency(1) == TestCurrency(2))

#   with self.assertRaises(TypeError):
#     TestCurrency(1) >  DemoCurrency(1)
#   with self.assertRaises(TypeError):
#     TestCurrency(1) >= DemoCurrency(1)
#   with self.assertRaises(TypeError):
#     TestCurrency(1) <  DemoCurrency(1)
#   with self.assertRaises(TypeError):
#     TestCurrency(1) <= DemoCurrency(1)

#   # math

#   with self.assertRaises(TypeError):
#     TestCurrency(1) + str()
#   with self.assertRaises(TypeError):
#     TestCurrency(1) - str()

#   self.assertEqual(DemoCurrency(1) + DemoCurrency(2), DemoCurrency(3))
#   self.assertEqual(DemoCurrency(3) - DemoCurrency(2), DemoCurrency(1))

#   self.assertEqual(2*DemoCurrency(2), DemoCurrency(4))
#   self.assertEqual(DemoCurrency(2) * 2, DemoCurrency(4))
#   self.assertEqual(DemoCurrency(2) * 2.0, DemoCurrency(4))
#   self.assertEqual(DemoCurrency(2) * Decimal('2.0'), DemoCurrency(4))

#   with self.assertRaises(TypeError):
#     TestCurrency(1) * TestCurrency(1)

#   self.assertEqual(DemoCurrency(8) // Decimal('2.0'), DemoCurrency(4))
#   self.assertEqual(DemoCurrency(8) // 2.0, DemoCurrency(4))
#   self.assertEqual(DemoCurrency(8) // 2, DemoCurrency(4))
#   self.assertEqual(DemoCurrency(8) // DemoCurrency(2), Decimal(4))

#   self.assertTrue( isinstance(DemoCurrency(8) // DemoCurrency(2), Decimal))

#   with self.assertRaises(TypeError):
#     TestCurrency(1) // DemoCurrency(1)

#   # text output

#   self.assertEqual(repr(TestCurrency()), "<TestCurrency: 'Currency'>")
#   self.assertEqual(repr(DemoCurrency(1)), "<DemoCurrency: '1.00 $'>")

#   obj1 = TestCurrency()
#   self.assertEqual(str(obj1), "Currency")

#   obj1.set('23.00')
#   obj2 = TestCurrency(Decimal(23))
#   self.assertEqual(str(obj1), str(obj2))