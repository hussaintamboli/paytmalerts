from unittest import TestCase

from paytmalerts.alerts import bus


class TestBus(TestCase):

    def test_available(self):
        self.assertIsNone(bus.available('2016-09-10', 'pune', 'latur', 'travelsName', 'vivekanand'))