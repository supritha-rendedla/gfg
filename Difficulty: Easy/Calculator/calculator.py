class Solution:
    def calculate(self, a: int, b: int, operator: int)-> None:
        #code here
        if operator==1:
            print(a+b,end="")
        elif operator==2:
            print(b-a,end="")
        elif operator==3:
            print(a*b,end="")
        else:
            print("Invalid Input")