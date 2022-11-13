for i in range(1,100):
    ages = str(i)

def is_palindrome(x,y):
    return x[::-1] == y


def main():
    z = 15
    while z <= 45:
        palindromes = []
        for i in range(100):
            if (i + z) >= 99:
                pass
            elif is_palindrome(ages[i],ages[i+z]):
                palindromes.append(ages[i])

        if len(palindromes) == 8:
            return palindromes
        else:
            z += 1

candidates = main()

print('your age is {} years old'.format(candidates(5)))

