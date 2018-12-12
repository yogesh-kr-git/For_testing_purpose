a=1221
b=a
rev=0
while a !=0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
if b==rev:
    print("palindrome")
else:
    print("not palindrome")
    
