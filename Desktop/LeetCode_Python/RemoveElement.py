class Solution:
    def remove_element(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]

                k += 1

        return k

sol = Solution()

test_cases = [
    ([3,2,2,3], 3, 2),
    ([0,1,2,2,3,0,4,2], 2, 5),
    ([], 1, 0),
    ([1], 2, 1),
    ([1,1,1,1], 1, 0),
    ([1,2,3,4,5], 6, 5)

]

passed = 0
failed = 0

for nums, val, expected in test_cases:
    result = sol.remove_element(nums, val)

    if result == expected:
        print(f"Passed")
        passed += 1

    else:
        print(f"Failed")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)}")

