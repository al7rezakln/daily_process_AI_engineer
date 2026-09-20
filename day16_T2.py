l1 = ["ali", "python", "REZA", "", "   ", "programming"]

def predicate(strings: list[str]) -> list[str]:
    """
    Reads a list of strings ,fliters the empty ones and capitalize the remaining ones using python funcs.
    Personaly prefer this to predicate 2 because it is more profesional than doing it with comprehension.
    Parameters:
        strings (str): Reads a list of random strings that may be some empty strings among them.
    Returns:
        list[str]: A list wich is a filtered and capitalized version of input that has no empty sttrings. 
    """
    l_01 = list(map(lambda s: s.capitalize(), filter(lambda s: s.strip()!="", strings)))
    return l_01

l2 = predicate(l1)

def predicate2(strings: list[str]) -> list[str]:
    """
        Reads a list of strings ,fliters the empty ones and capitalize the remaining ones using comprehensions.
        
        Parameters:
            strings (str): Reads a list of random strings that may be some empty strings among them.
        Returns:
            list[str]: A list wich is a filtered and capitalized version of input that has no empty sttrings. 
        """
    l_01 = [string.strip() for string in strings if string.strip()!=""]
    l_02 = [string.capitalize() for string in l_01]
    return l_02

print(predicate2(l1))