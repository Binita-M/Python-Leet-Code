class Solution:
    def canJump(self, nums:list[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True

sol = Solution()

test_cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([0], True),
    ([1], True),
    ([1,0], True),
    ([0,1], False),
    ([0,0,0,0], False),
    ([1,1,1,1], True),
    ([10, 0,0,0,0], True),
    ([1,0,1,0,1], False),
    ([1,1,1,1,1], True),
    ([2]* 10000, True),
    ([1,2,3,0], True),
    ([5,4,3,2,1,0], True),
]

passed = 0
failed = 0

for nums, expected in test_cases:
    result = sol.canJump(nums)
    display = str(nums[:6])[:-1] + (', ...]' if len(nums) > 6 else ']')
    if result == expected:
        print(f"Passed: {display} -> {result}")
        passed += 1
    
    else:
        print(f"Failed: {display} -> {result}")
        failed += 1

print(f"\n{passed} passed, {failed} failed out of {len(test_cases)} tests")