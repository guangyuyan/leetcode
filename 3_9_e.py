#!/usr/bin/python
# -*- coding: UTF-8 -*-


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # if x < 0 | x % 10 == 0:
    #     return False
    # elif str(x) == str(x)[::-1]:
    #     return True
    # else:
    #     return False
    # x_a = x


print(isPalindrome(121))

###method2###


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    x_a = x
    x_new = 0
    n = 0
    while x_a > x_new:
        x_new = x_new * 10 + int(x_a % 10)
        x_a = int(x_a / 10)
        n += 1
    if x_a == int(x_new / 10) or x_a == x_new:
        return True
    else:
        return False