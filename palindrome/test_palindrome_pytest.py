import pytest
import palindrome

class TestCalc:
    def test_addition(self):
        assert palindrome.isPalindrome("ab $ ba") == True
        assert palindrome.isPalindrome("abcb a") == False
        assert palindrome.isPalindrome("asd dsa!") == True

