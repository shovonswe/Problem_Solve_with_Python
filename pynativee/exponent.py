def exponent (base, expo):

 num = expo
 result = 1
 while num>0:
        result = result* base
        num = num-1
 return result
    

n1 = int(input("base = "))

n2 = int(input("exponent = "))

print(n1, "raises to the power of", n2,"is: ",exponent(n1,n2))
