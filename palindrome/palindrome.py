from operator import truediv
from pickle import FALSE


def isPalindrome(inputString):
    i = 0

    inputString = inputString.lower()

    for ele in range(len(inputString)):
        if inputString[ele] == inputString[len(inputString)- 1 - i]:
            i = i + 1

    if i == len(inputString):
        return True
    else:
        return False