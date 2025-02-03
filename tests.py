import unittest
from add_sum import add


class TestAddFunction(unittest.TestCase):
    """
    Unit testcase for the add sum function
    """
    def test_empty_string(self):
        """edge case for empty string"""
        self.assertEqual(add(""), 0)
    
    def test_basic_comma_separated_numbers(self):
        """all positive number case"""

        self.assertEqual(add("1,2,3,4,5"), 15)
    
    def test_newline_and_comma_separated_numbers(self):
        """ test \n as a default delimiter """
        self.assertEqual(add("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        """custom delimiter"""
        self.assertEqual(add("//;\n1;2;3;9"), 15)
    
    def test_ignore_numbers_greater_than_1000(self):
        """ignore numbers greater than 1000"""
        self.assertEqual(add("1001,2,3"), 5)
    
    def test_negative_numbers_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertIn("Negative numbers are not allowed", str(context.exception))
    
    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("-1,-2,-3")
        self.assertIn("Negative numbers are not allowed", str(context.exception))
    
    def test_custom_delimiter_with_special_characters(self):
        self.assertEqual(add("//***\n1***2***3"), 6)

# run the unit tests
if __name__ == '__main__':
    unittest.main()