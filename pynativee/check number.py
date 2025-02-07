list_x=list(map(int,input("give me some numbers seperated by space: ").split()))

list_y=[6,7,8,9,10]

length=len(list_x)

if(list_x[0]==list_x[length-1]):
  
  print("true")
else:
  print("false")