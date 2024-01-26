#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys

"""
type hints:
Example:
    def is_positive(n: int) -> bool:

Means:
    The argument `n` is an `int` and the return value is a `bool`
"""


# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * 3  # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + "!!!"
    return result


# Gather our code in a main() function
def main():
    # print('Hello there', sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    print(repeat("Yay", False))  ## YayYayYay
    print(repeat("Woo Hoo", True))  ## Woo HooWoo HooWoo Hoo!!!


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
    main()
