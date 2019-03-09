def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n_length = len(needle)
    h_length = len(haystack)
    if n_length > h_length:
        return -1
    if n_length == 0:
        return 0

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            t = True
            for j in range(1, n_length):
                if i + j >= h_length:
                    return -1
                if haystack[i + j] != needle[j]:
                    t = False
                    break
            if t == True:
                return i

    return -1