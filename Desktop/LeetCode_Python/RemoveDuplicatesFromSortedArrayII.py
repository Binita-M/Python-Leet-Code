class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        k = 0

        for num in nums:
            if k < 2 or num != nums[k-2]:
                nums[k] = num
                k += 1

        return k

sol = Solution()

test_cases = [
    ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
    ([0,0,1,1,1,2,2,3], 7, [0,0,1,1,2,2,3]),
    ([1], 1, [1]),
    ([1,1], 2, [1,1]),
    ([1,2,3,4,5], 5, [1,2,3,4,5]),
    ([3,3,3,3,3], 2, [3,3]),
    ([1,1,2,2,3,3], 6, [1,1,2,2,3,3]),
    ([-3,-3,-3,-1,-1,0,0,0, 1,1,2,2,2], 10, [-3,-3,-1,-1,0,0,1,1,2,2])
]

passed = 0
failed = 0

for nums, expected_k, expected_nums in test_cases:
    result = sol.remove_duplicates(nums)

    if result == expected_k and nums[:result] == expected_nums:
        print(f"Passed")
        passed += 1

    else:
        print(f"Failed")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)} cases")
