import unittest
from random_quote_generator.app import fetch_random_quote, save_favorite_quote

class TestApp(unittest.TestCase):
    def test_fetch_random_quote(self):
        """Test that fetch_random_quote returns a valid quote."""
        quote = fetch_random_quote()
        self.assertIsInstance(quote, str)
        self.assertTrue(len(quote) > 0)

    def test_save_favorite_quote(self):
        """Test that save_favorite_quote writes to the file."""
        test_quote = "Test Quote - Test Author"
        save_favorite_quote(test_quote)
        
        # Verify the quote was saved to the file
        with open("favorite_quotes.txt", "r") as file:
            saved_quotes = file.readlines()
        
        self.assertIn(test_quote + "\n", saved_quotes)

if __name__ == "__main__":
    unittest.main()

