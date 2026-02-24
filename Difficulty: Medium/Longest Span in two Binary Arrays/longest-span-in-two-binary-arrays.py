class Solution:
    def equalSumSpan(self, a1, a2):

        mp = {0: -1}
        prefix = 0
        max_len = 0

        for i in range(len(a1)):
            prefix += a1[i] - a2[i]

            if prefix in mp:
                max_len = max(max_len, i - mp[prefix])
            else:
                mp[prefix] = i

        return max_len