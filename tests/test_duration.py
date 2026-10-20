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

    def test_two_hours(self):
        self.assertEqual(format_duration(120), "2時間")

    def test_three_hours(self):
        self.assertEqual(format_duration(180), "3時間")

    def test_four_hours_review_seed(self):
        self.assertEqual(format_duration(240), "4時間")


if __name__ == "__main__":
    unittest.main()
