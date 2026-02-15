#User function Template for python3

class Solution:

    def findMinDiff(self, arr,m):
        a=len(arr)
        if m == 0 or a == 0 or m > a:
            return 0
        arr.sort()
        low_diff = float("inf")
        for i in range(a-m+1):
            d = arr[i+m-1] - arr[i]
            if d < low_diff:
                low_diff = d
        return low_diff
        