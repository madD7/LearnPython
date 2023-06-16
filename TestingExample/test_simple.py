import unittest
import simple

"""
Test class must inherit class - unittest.TestCase
"""
class MyTestCase(unittest.TestCase):
    def test_single_word(self):
        test_text = 'python'
        result = simple.my_capitalize_func(test_text)
        self.assertEqual(result, 'Python')  # add assertion here

    def test_multiple_words(self):
        test_text = 'python example code test'
        expected_result = 'Python example code test'
        result = simple.my_capitalize_func(test_text)
        self.assertEqual(result, expected_result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
