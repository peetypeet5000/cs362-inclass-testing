import unittest
import wordCount

class TestCase(unittest.TestCase):
    def test_wordCount(self):
        self.assertEqual(wordCount.wordCount("This is four words."), 4)
        self.assertEqual(wordCount.wordCount(" space before first word and after last "), 7)
        self.assertEqual(wordCount.wordCount("connecting_words-with_chars and&symbols"), 6)

#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)