import argparse
import os
import re
from collections import Counter
DEFAULT_TOP_NUM = 1

def parse_txt_file(filepath: str) -> list[str]:
    """
    Reads a text file and extracts all words in lowercase.

    Parameters:
        filepath (str): The path to the text file.

    Returns:
        list[str]: A list of extracted words excluding numbers and punctuation.
    """
    with open(filepath) as file:
        return re.findall(r"\b[^\d\W]+\b", file.read().lower())

def counter_parsed_txt(parsed_txt: list[str]) -> dict[str, int]:
    """
    Counts the frequency of each word in the provided list.

    Parameters:
        parsed_txt (list[str]): A list of words.

    Returns:
        dict[str, int]: A dictionary with words as keys and their frequencies as values.
    """
    return dict(Counter(parsed_txt))

def get_unique_words(parsed_txt: list[str]) -> set[str]:
    """
    Extracts a unique set of words from the provided list.

    Parameters:
        parsed_txt (list[str]): A list of words.

    Returns:
        set[str]: A set containing only the unique words.
    """
    return set(parsed_txt)

def top_asked_words(top_asked: int, parse_counter: dict[str, int]) -> dict[str, int]:
    """
    Retrieves the most common words based on the specified count.

    Parameters:
        top_asked (int): The number of most common words to retrieve.
        parse_counter (dict[str, int]): A dictionary containing word frequencies.

    Returns:
        dict[str, int]: A dictionary of the most common words and their frequencies.
    """
    words_sorted = Counter(parse_counter).most_common(top_asked)
    return dict(words_sorted)

def main()-> tuple[set[str], dict[str, int]]:
    """
    Is a centeral function that connects every side function together

    Returns:
        List of a unique words in text file
        &
        Dictionary that contains some top wanted words
    """
    parser = argparse.ArgumentParser(description="Parsing a txt file.")
    parser.add_argument("filepath", help="Write down a txt-file", type=str)
    parser.add_argument("--top", type=int, default=DEFAULT_TOP_NUM, help="Write down top most common words you'd like to see")

    args = parser.parse_args()
    filepath = args.filepath
    top_asked = args.top

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found!")

    if os.path.getsize(filepath) == 0:
        raise ValueError("Text file is empty!")
    
    parsed_txt = parse_txt_file(filepath)    
    parse_counter = counter_parsed_txt(parsed_txt)

    return get_unique_words(parsed_txt), top_asked_words(top_asked, parse_counter)

if __name__ == "__main__":
    unique_words, asked_words = main()
    print(f"Number of unique words is : {len(unique_words)}")
    print(f"\033[32mTop {len(asked_words)} of most common words:\033[0m")
    for word, count in asked_words.items():
        print(f"{word}: {count}")