class Solution():
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1

            else:
                count -= 1

        return candidate

sol = Solution()

test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([1], 1),
    ([5,5,5,5,5], 5),
    ([7,7,7,7,7,7,7], 7),
    ([1,1,2], 1),
    ([-1,-1,-1,2,3], -1),
    ([-5,-5,1,2,-5], -5),
    ([-1,1,-1,-1,1,-1], -1),
    ([1,2,1,2,1,2,1,2,1], 1),
    ([3,3,4,3,4,3,4,3,4,3], 3)
]

passed = 0
failed = 0

for nums, expected in test_cases:
    result = sol.majorityElement(nums)

    if result == expected:
        print(f"Passed")
        passed += 1

    else:
        print(f"Failed")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)} cases")
