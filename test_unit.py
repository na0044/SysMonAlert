import unittest

class TestExample(unittest.TestCase):
    def test_example(self):
        print("Test is running...")
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()