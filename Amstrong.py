num = int(input("Enter the number"))
temp = num
digits = len(str(num))

sum = 0
while(temp != 0):
    digit = temp%10
    sum += digit**digits
    temp //= 10

if sum == num:
    print("The number is Amstrong")
else:
    print("Number is not amstrong")



