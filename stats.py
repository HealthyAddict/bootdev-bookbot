def count_words(text):
    number_of_words = len(text.split())
    return number_of_words

def count_letters(text):
    letter_counts = {}

    for char in text:
        char = char.lower()
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    return letter_counts

def sort_characters(char_count):
    sorted_chars = []

    for char, count in char_count.items():
        sorted_chars.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars