def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    def rm_zero(z):
        if z[-1] == '0':
            return rm_zero(z[0:-1])
        else:
            return z

    def recursive_num(y):
        y_rm_zero = rm_zero(y)
        return int(y_rm_zero[::-1])

    def main(x):
        if x < 0:
            x_pos_str = str(x)[1:]
            return 0 - recursive_num(x_pos_str)
        else:
            x_pos_str = str(x)
            return recursive_num(x_pos_str)

    if x == 0:
        return 0

    res = main(x)
    if (res < -(2 ** 31)) | (res >= 2 ** 31):
        return 0
    else:
        return res
