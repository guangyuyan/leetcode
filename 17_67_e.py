class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ins = 0  # 进位
        res = []
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        while a and b:
            val = a.pop() + b.pop() + ins
            res.append(val % 2)
            ins = val / 2

        if b:
            a = b
        while a:
            val = a.pop() + ins
            res.append(val % 2)
            ins = val / 2
        if ins == 1:
            res.append(ins)

        res = res[::-1]
        res = map(str, res)
        return "".join(res)
