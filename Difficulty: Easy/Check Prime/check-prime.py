#User function Template for python3
n = int(input())

# Your code here
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("True")
else:
    print("False")