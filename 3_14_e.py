class Solution:
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        idx_1 = 0
        prefix = ''
        break_flag = 0
        if len(strs) == 0 or '' in strs:
            return prefix
        if len(strs) == 1:
            return strs[0]
        min_len = sorted(list(map(len, strs)))[0]
        while idx_1 < min_len:
            if break_flag:
                break
            idx_2 = 0
            while idx_2 < len(strs):
                if strs[0][idx_1] == strs[idx_2][idx_1]:
                    if idx_2 == len(strs) - 1:
                        prefix = prefix + strs[0][idx_1]
                else:
                    break_flag = True
                    break
                idx_2 += 1
            idx_1 += 1
        return prefix