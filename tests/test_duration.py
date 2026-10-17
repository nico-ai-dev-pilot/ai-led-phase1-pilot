import unittest

from duration import format_duration


class DurationTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_duration(0), "0分")

    def test_minutes(self):
        self.assertEqual(format_duration(30), "30分")

    def test_one_hour(self):
        self.assertEqual(format_duration(60), "1時間")

    def test_hours_and_minutes(self):
        self.assertEqual(format_duration(90), "1時間30分")


if __name__ == "__main__":
    unittest.main()
