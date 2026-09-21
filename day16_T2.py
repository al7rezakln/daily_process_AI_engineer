def is_non_blank(string: str) -> bool:
    """
    This func checks if every string in its input is empty or not.
    Parameters:
        string(str): The string that the func checks if its empty or not.

    Returns:
        bool: If the string is empty it returns False and if it's not it returns True. 
    """
    return string.strip() != ""
    

def format_string(s: str) -> str:
    """
    Removes leading/trailing whitespaces and capitalizes the first character of the string.

    Parameters:
        s (str): The input string to be formatted.

    Returns:
        str: The cleaned string with no surrounding space and the first letter capitalized.
    """
    return s.strip().capitalize()

def clean_with_functional(strings: list[str]) -> list[str]:
    """
    Filters out blank strings and formats the remaining non-blank items using functional programming.

    Parameters:
        strings (list[str]): A list of input strings to be processed.

    Returns:
        list[str]: A list of non-blank, formatted strings.
    """   
    res = list(filter(is_non_blank, strings))
    res = list(map(format_string, res))
    return res

def clean_with_comprehension(strings: list[str]) -> list[str]:
    """
    Filters out blank strings and formats the remaining non-blank items using list comprehensions.

    Parameters:
        strings (list[str]): A list of input strings to be processed.

    Returns:
        list[str]: A list of non-blank, formatted strings.
    """
    res = [format_string(string) for string in strings if is_non_blank(string)]
    return res