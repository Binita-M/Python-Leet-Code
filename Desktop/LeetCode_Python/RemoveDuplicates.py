class Solution:
    def remove_duplicates(self, nums):
        k = 0

        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k

sol = Solution()

test_cases = [
    ([[1,2,2,3,4,5], 5]),
    ([0,0,1,1,2,2,3,3,4,4,5,5], 6),
    ([1], 0),
    ([1,2,3,4,5], 5),
    ([1,1,1,1,1], 0),
    ([1,1,2,2,3,3,4,5], 5),
    ([-1, -1, -2, 3, 4, 7], 5)
]

passed = 0
failed = 0

for nums, expected in test_cases:
    result = sol.remove_duplicates(nums)

    if result == expected:
        print(f"Passed")
        passed += 1

    else:
        print(f"Failed")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)}")