class solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0

        for num in nums:
            if k < 2 or num != nums[k-2]:
                nums[k] = num
                k += 1
        return k

sol = solution()

test_cases = [
    ([1,1,1,2,2,3], [1,1,2,2,3]),
    ([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3]),
    ([1], [1]),
    ([1,1], [1,1]),
    ([1,2], [1,2]),
    ([1,2,3,4,5], [1,2,3,4,5]),
    ([3,3,3,3,3], [3,3]),
    ([1,1,2,2,3,3], [1,1,2,2,3,3]),
    ([-3,-3,-3,-1,-1,0,0,0,2], [-3,-3,-1,-1,0,0,2]),
]

for nums, expected in test_cases:
    nums = nums[:]
    k = sol.removeDuplicates(nums)
    assert k == len(expected), f"Failed length: got {k}, expected {len(expected)}"
    assert nums[:k] == expected, f"Failed values: got {nums[:k]}, expected{expected}"
    print(f"PASSED: {expected}")




