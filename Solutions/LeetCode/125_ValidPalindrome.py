import re

def ValidPalindrome(sentence):
    trimmed = re.sub('[^0-9a-z]','',sentence.lower())
    reversed_trimmed = trimmed[::-1]

    if reversed_trimmed == trimmed:
        return True

    return False

print(ValidPalindrome("A man, a plan, a canal : Panama"))
print(ValidPalindrome("race a car"))