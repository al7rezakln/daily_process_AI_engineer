l1 = ["ali", "python", "REZA", "", "   ", "programming"]

def predicate(strings: list[str]) -> list[str]:
    l1 = list(map(lambda s: s.capitalize(), filter(lambda s: s.strip()!="", strings)))
    return l1

print(predicate(l1))