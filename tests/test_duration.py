import unittest

from duration import format_duration


class DurationTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_duration(0), "0分")

    def test_minutes(self):
        self.assertEqual(format_duration(30), "30分")


if __name__ == "__main__":
    unittest.main()
