import os
import random

# List of hardcoded quotes
QUOTES = [
    '"The best way to predict the future is to create it." - Peter Drucker',
    '"Life is what happens when you\'re busy making other plans." - John Lennon',
    '"Believe you can and you\'re halfway there." - Theodore Roosevelt',
    '"It does not matter how slowly you go as long as you do not stop." - Confucius',
    '"Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill',
    '"The only way to do great work is to love what you do." - Steve Jobs',
    '"In the middle of every difficulty lies opportunity." - Albert Einstein',
    '"Do not wait to strike till the iron is hot; but make it hot by striking." - William Butler Yeats',
]

def fetch_random_quote():
    """Fetch a random quote from the hardcoded list."""
    return random.choice(QUOTES)

def save_favorite_quote(quote):
    """Save a favorite quote to a local file."""
    favorites_file = "favorite_quotes.txt"
    try:
        with open(favorites_file, "a") as file:
            file.write(quote + "\n")
        print(f"Quote saved to {favorites_file}")
    except Exception as e:
        print(f"Failed to save quote: {e}")

def main():
    """Main function to run the quote generator."""
    print("Welcome to the Random Quote Generator!")
    while True:
        print("\nFetching a random quote...")
        quote = fetch_random_quote()
        print(f"\n{quote}")
        
        choice = input("\nDo you want to save this quote? (yes/no/exit): ").strip().lower()
        if choice == "yes":
            save_favorite_quote(quote)
        elif choice == "exit":
            print("Thank you for using the Random Quote Generator!")
            break

if __name__ == "__main__":
    main()

