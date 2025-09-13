


def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(item):
    return item["num"]

def sort_chars(counts):
    char_list = []
    for char, num in counts.items():
        if char.isalpha():   # keep only letters
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_char_counts(text):
    counts = {}
    for char in text.lower():
        if char in counts:  # Consider only alphabetic characters
            counts[char] += 1
        else:
            counts[char] = 1        

    return counts