def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dict = {'(': ')', '[': ']', '{': '}'}
    list = []

    for element in s:
        if element in dict:
            list.append(element)
        elif len(list) > 0 and element == dict[list[-1]]:
            list.pop(-1)
    if len(list) == 0:
        return True
    else:
        return False

print(isValid(')['))