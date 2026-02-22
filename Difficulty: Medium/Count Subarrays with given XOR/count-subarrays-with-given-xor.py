class Solution:
    def subarrayXor(self, arr, k):
        # code here
        freq = {}
        xr = 0
        count = 0

        for num in arr:
            xr ^= num

            # case 1: prefix XOR itself equals k
            if xr == k:
                count += 1

            # case 2: find previous prefix XOR
            need = xr ^ k
            if need in freq:
                count += freq[need]

            # store prefix XOR
            freq[xr] = freq.get(xr, 0) + 1

        return count