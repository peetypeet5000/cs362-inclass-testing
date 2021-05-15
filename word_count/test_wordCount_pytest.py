import pytest
import wordCount

class TestWordCount:
    def test_wordCount(self):
        assert wordCount.wordCount("this is simply five words") == 5
        assert wordCount.wordCount("!!starting with symbols!!!") == 3
        assert wordCount.wordCount("    lots of spaces!") == 3
