#User function Template for python3
# Take year input and print if year is a leap year
year=int(input())
if year%400==0:
    print("True")
elif year%100==0:
    print("False")
elif year%4==0:
    print("True")
else:
    print("False")
        