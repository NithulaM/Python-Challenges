num = int(input("Enter a number"))
temp = num
rev = 0

while temp != 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == num:
    print("The number is Palindrome")
else:
    print("The number is not palindrome")


