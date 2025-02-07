def merge_list(list1,list2):
    result = []
    for num in list1:
     if (num%2==0):
       result.append(num)

    for num in list2:   
      if (num%2==0):
       result.append(num)
    return result

list1 = list(map(int,input("give me numbers").split()))
list2 = list(map(int,input("give me numbers").split()))
print("result list:", merge_list(list1, list2))    