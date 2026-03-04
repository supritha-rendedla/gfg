class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Step 1: Compute XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        
        max_xor = current_xor
        
        # Step 2: Slide the window
        for i in range(k, n):
            current_xor ^= arr[i - k]  # Remove left element
            current_xor ^= arr[i]      # Add new element
            
            max_xor = max(max_xor, current_xor)
        
        return max_xor
        
        
       