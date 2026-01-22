class Solution:
    def printPattern(self, n):
        for i in range(1,n):
            if i==1:
                print("*")
            else:
                print("*"+" "*(2*(i-2)+1)+"*")
        print("* "*n)