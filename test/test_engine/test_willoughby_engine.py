import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_return_true(self):
        self.assertTrue(WilloughbyEngine(60003, 0).needs_service())

    def test_needs_service_return_false(self):
        self.assertFalse(WilloughbyEngine(60000, 0).needs_service())
