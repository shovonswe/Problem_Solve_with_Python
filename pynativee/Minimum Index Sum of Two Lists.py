class Solution:
    
    def findRestaurant(self, list1,list2):
        list_map = {value1: i1 for i1, value1 in enumerate(list1)}
        min_value = float('inf')
        result = []

        for i2, value2 in enumerate(list2):
            if value2 in list_map:
                index_sum = i2 + list_map [value2]
                if min_value > index_sum:
                    min_value = index_sum
                    result = [value2]
                elif min_value == index_sum:
                       result.append(value2)
        return result               




Solution = Solution()
list1 = ["happy","sad","good"]
list2 =  ["sad","happy","good"]
print(Solution.findRestaurant(list1,list2))