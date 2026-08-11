class Solution:
    def rotate(self, nums: list[int], k:int) -> None:
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

sol = Solution()

test_cases = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1, -100, 3, 99], 2, [3,99,-1,-100]),
    ([1,2,3], 0, [1,2,3]),
    ([1,2,3], 4, [3,1,2]),
    ([1], 5, [1]),
    ([1,2], 2, [2,1]),
    ([1,2], 2, [1,2]),
    ([5,5,5,5], 2, [5,5,5,5]),
    ([-1,-2,-3,-4], 2, [-3,-4,-1,-2]),
    ([1,2,3,4,5], 100, [1,2,3,4,5]),
]

passed = 0
failed = 0

for nums, k, expected in test_cases:
    nums = nums[:]
    sol.rotate(nums, k)
    if nums == expected:
        print(f"Passed: {nums} (k={k})")
        passed += 1
    else:
        print(f"Failed: got{nums}, expected {expected} (k={k})")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)} tests")