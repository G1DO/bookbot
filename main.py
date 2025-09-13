import sys
from stats import get_num_words, get_char_counts, sort_chars    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    
    # word count
    num_words = get_num_words(text)
  
    print(f"Analyzing book found at {path}...")
   
    print(f"Found {num_words} total words")

    # character count
    counts = get_char_counts(text)
    sorted_counts = sort_chars(counts)
   
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")

  


main()
