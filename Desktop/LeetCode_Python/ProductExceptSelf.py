class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

sol = Solution()

test_cases = [
    ([1,2,3,4], [24,12,8,6]),          # basic case from problem
    ([-1,1,0,-3,3], [0,0,9,0,0]),      # one zero
    ([2,3], [3,2]),                    # two elements
    ([5], [1]),                        # single element -> no other elements, product = 1
    ([1,1,1,1], [1,1,1,1]),            # all ones
    ([2,2,2,2], [8,8,8,8]),            # all same value
    ([0,0], [0,0]),                    # two zeros -> everything is 0
    ([0,4,0], [0,0,0]),                # two zeros, nonzero in between
    ([-1,-2,-3,-4], [-24,-12,-8,-6]),  # all negative
    ([1,-1,1,-1], [1,-1,1,-1]),        # alternating signs
    ([3,0], [0,3]),                    # zero at the end
    ([0,3], [3,0]),                    # zero at the start
]

passed = 0
failed = 0

for nums, expected in test_cases:
    result = sol.product_except_self(nums)

    if result == expected:
        print(f"Passed")
        passed += 1
    else:
        print(f"Failed")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)} test cases")