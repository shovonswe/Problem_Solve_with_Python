#optimal:(sliding_window)
class Solution:
     def numOfSubarrays(self, arr,k,r):
          n = len(arr)
          window_sum = sum(arr[:k])
          count = 0
          if window_sum/k >= r:
               count += 1
          for i in range(k,n):
               window_sum += arr[i]
               window_sum -= arr[i-k]
               if window_sum/k >= r:
                    count += 1
          return count               
solution = Solution()
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
r = 5
print(solution.numOfSubarrays(arr,k,r))


#brute force.
# class Solution:
#     def numOfSubarrays(self, arr,k,r):
#        n =len(arr)
#        count = 0
#        avg = 0
#        for i in range(n-(k-1)):
#            window_sum = 0
#            for  j in range(i, i+k):
#              window_sum  += arr[j]
#            avg = window_sum/k 
#            if avg >= r:
#                   count += 1
            
#        return  count          
                      
# solution = Solution()
# arr = [11,13,17,23,29,31,7,5,2,3]
# k = 3
# r= 5  
# print(solution.numOfSubarrays(arr,k,r))
