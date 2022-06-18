import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_return_true(self):
        self.assertTrue(SternmanEngine(True).needs_service())

    def test_needs_service_return_false(self):
        self.assertFalse(SternmanEngine(False).needs_service())
