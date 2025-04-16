class solution:
     def replaceElements(self, arr):
          max_from_right = -1
          for i in range(len(arr)-1, -1, -1):
               current = arr[i]
               arr[i] = max_from_right
               max_from_right = max(max_from_right,current)
          return arr
           
solution = solution()       
arr = [17,18,5,4,6,1]
print(solution.replaceElements(arr))