class Solution:
    def largestSwap(self, s):
        #code here
        s = list(s)
        last = {int(d): i for i, d in enumerate(s)}
        
        for i in range(len(s)):
            for d in range(9, int(s[i]), -1):
                if d in last and last[d] > i:
                    j = last[d]
                    s[i], s[j] = s[j], s[i]
                    return "".join(s)
        
        return "".join(s)
        