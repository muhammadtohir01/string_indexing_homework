def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    l1=s[0:1]
    l2=s[len(s)-1:len(s)]
    b=l1+l2
    return b
print(main('salom'))