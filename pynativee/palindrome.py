num = input("")
print("original number is: ",num)

if(num==num[::-1]):
    print("palindrome")
else:
    print("not palindrome")
