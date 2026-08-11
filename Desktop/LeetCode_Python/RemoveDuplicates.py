class solution(object):
    def removeDuplicates(self, nums):
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k

#Test cases
sol = solution()

test_cases = [
    ([1,1,2], 2, "Example 1 - basic duplicates"),
    ([0,0,1,1,1,2,2,3,3,4], 5, "Example 2 - multiple duplicates"),
    ([1], 1, "Single Element"),
    ([1,2,3,4,5], 5, "No duplicates"),
    ([1,1,1,1,1], 1, "All same elements"),
    ([-3,-2,-1,0,0,1], 5, "Negative numbers"),
    ([1,1,2,2,3,3], 3, "All pairs"),
]

for nums, expected_k, description in test_cases:
    result = sol.removeDuplicates(nums)
    if result == expected_k:
        print(f"PASSED | {description}")
    
    else:
        print(f"FAILED | {description}")

