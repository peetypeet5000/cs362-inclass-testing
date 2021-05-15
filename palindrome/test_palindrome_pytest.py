import pytest
import palindrome

class TestPalindrome:
    def test_palindrome(self):
        assert palindrome.isPalindrome("ab $ ba") == True
        assert palindrome.isPalindrome("abcb a") == False
        assert palindrome.isPalindrome("asd dsa!") == True

