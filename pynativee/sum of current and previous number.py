 start = int(input("star from :"))
 end = int(input("end here : "))
 sum = 0
 for i in range(start,end+1):
  sum = i+(i-1)
  print("curreent number : ",i, "previous number",i-1,"sum :",sum)

  