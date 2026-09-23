import argparse

def split_and_sum(*args: int)-> str:
    """Splits the first argument from the rest and calculates the sum of the remaining numbers.

    Args:
        *args (int): A sequence of integers. At least one integer is required.

    Returns:
        str: A formatted string displaying the first number and the sum of the remaining numbers.

    Raises:
        ValueError: If no arguments are provided.
    """
    first, *rest = args    
    return f"first: {first}, total of rest: {sum(rest, start=0)}"

def main() -> str:
    """Parses command-line arguments and executes the split_and_sum function.

    Reads a list of integers passed via the terminal, unpacked as positional
    arguments, and passes them to split_and_sum.

    Returns:
        str: The output string produced by split_and_sum.
    """
    parser = argparse.ArgumentParser(description="Getting more than one argument.")
    parser.add_argument("items", nargs='+', help="Enter one or more numbers.", type=int)
    args = parser.parse_args()
    return split_and_sum(*args.items)

if __name__ == "__main__":
    print(main())