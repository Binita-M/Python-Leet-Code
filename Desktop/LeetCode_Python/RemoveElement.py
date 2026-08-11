class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    
    # ---- TEST ----
sol = Solution()  # create an instance of the class

test_cases = [
    ([3,2,2,3],         3, 2, "Basic - remove 3s"),
    ([0,1,2,2,3,0,4,2], 2, 5, "Remove 2s"),
    ([],                1, 0, "Empty array"),
    ([1],               1, 0, "Single element removed"),
    ([1],               2, 1, "Single element kept"),
    ([2,2,2,2],         2, 0, "All removed"),
    ([1,2,3,4],         5, 4, "Nothing removed"),
]

for nums, val, expected_k, description in test_cases:
    result = sol.removeElement(nums, val)  # call via sol.removeElement
    if result == expected_k:
        print(f"PASSED | {description}")
    else:
        print(f"FAILED | {description} → got {result}, expected {expected_k}")