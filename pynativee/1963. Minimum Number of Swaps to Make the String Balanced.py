class Solution:
    def minSwaps(Self,str):
        need = 0
        count = 0
        for char in str:
            if(char == ']'):
                count += 1
            else:
                count -= 1
            need = max(need,count)
        return (need+1)//2 
sol = Solution()
s = "]]][[["
print(sol.minSwaps(s))                 