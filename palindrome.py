a=121
t=a
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
if t==rev:
    print("Palindrome")
else:
    print("Not an palindrome")