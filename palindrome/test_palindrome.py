import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome.isPalindrome("Madam, I'm Adam"), True)
        self.assertEqual(palindrome.isPalindrome("ab55ba"), True)
        self.assertEqual(palindrome.isPalindrome("Refer"), True)

#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)