# s = "PYnative"
# print(s[2:]) # "native" - From index 2 to the end
# print(s[:4])#"PYna"- From the beginning index 4(exclusive)
# print(s[1:5])# "Ynat"   - From index 1 to index 5 (exclusive)

def remove_strs(s,n):
   
    return  s[n:]



str = input("give me a string:" )
n = int (input("give me a number"))
print(remove_strs(str,n))