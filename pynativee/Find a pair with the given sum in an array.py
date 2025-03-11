def find_pair_brute_force(nums, target):
    found = False
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  
            if nums[i] + nums[j] == target:
                print(f"Pair found ({nums[i]}, {nums[j]})")
                found = True
    if not found:            
     print("Pair not found") 


nums1 = [8, 7, 2, 5, 3, 1]
target1 = 10
find_pair_brute_force(nums1, target1)

nums2 = [5, 2, 6, 8, 1, 9]
target2 = 12
find_pair_brute_force(nums2, target2)
