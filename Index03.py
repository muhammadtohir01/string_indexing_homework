def main(s):
    """
    The string variable s is given. return the last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[len(s)-1:len(s)]
print(main('codeschooluz'))