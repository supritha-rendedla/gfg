class Solution:    
    def findUnion(self, a, b):
        # code here
        s = set(a)      
        s.update(b)     
        return list(s)