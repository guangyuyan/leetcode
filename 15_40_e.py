def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    rest = []

    def depthc(tempn, i):
        for num in range(i, len(candidates)):
            temp = tempn - candidates[num]
            if temp > 0:
                rest.append(candidates[num])
                depthc(temp, num + 1)
                rest.pop()
            elif temp == 0:
                rest.append(candidates[num])
                restemp = rest[:]
                restemp.sort()
                if restemp not in res:
                    res.append(restemp)
                rest.pop()

        return res

    return depthc(target, 0)