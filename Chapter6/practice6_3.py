def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(first('noon'))
print(last('noon'))
print(middle('noon'))

#test
print(middle('ed')) #middle()调用两个字母的单词，返回空值
print(middle('a'))  #依旧是空
print(middle(''))  #还是空

def is_palindrome(string):
    if len(string) == 0:
        print("字符串不可以为空")
        return None
    elif len(string) == 2:
        print("字符串必须多余于两个字母")
        return None
    else:
        if len(middle(string)) > 0 and (first(string) == last(string)):
            n = len(middle(string))
            if middle(string)[n] == middle(string)[-(n-1)]:
                return True
        else:
            return False

print(is_palindrome('dad'))

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('noon'))






        

