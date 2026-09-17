import argparse, re
from collections import Counter
DEFAULT_TOP_NUM = 1

parser = argparse.ArgumentParser(description="Parsing a txt file.")
parser.add_argument("filepath", help="Write down a txt-file", type=str)
parser.add_argument("--top", type=int, default=DEFAULT_TOP_NUM, help="Write down top most common words you'd like to see")

args = parser.parse_args()
filepath = args.filepath
top_asked = args.top

def parse_txt_file(filepath: str) -> list[str]:
    with open(filepath) as file:
        return re.findall(r"\b\w+\b", file.read().lower())

parsed_txt = parse_txt_file(filepath)
def counter_parsed_txt(parsed_txt: list[str]) -> dict[str, int]:
    return dict(Counter(parsed_txt))

def top_asked_words(top_asked: int) -> str:
    #words_with_num = counter_parsed_txt(parsed_txt)
    #words_with_num = sorted(words_with_num.items(), key=lambda s: s[1], reverse=True) همون دو خط بعدیه ولی دو خط بعد رو با تابع آماده نوشتم
    temp001 = counter_parsed_txt(parsed_txt)
    words_sorted = Counter(temp001).most_common(top_asked)
    return dict(words_sorted)

print(top_asked_words(top_asked))