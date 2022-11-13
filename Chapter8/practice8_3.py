def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if word != word[:]:
        return False
    return True

print(is_palindrome('noon'))