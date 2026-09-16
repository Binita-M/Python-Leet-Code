class Solution():
    def merge_sort(self, nums1, m, nums2, n):
        p1, p2, p3 = (m-1, n-1, m+n-1)

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1

            else:
                nums1[p3] = nums2[p2]
                p2 -= 1

            p3 -= 1

sol = Solution()

passed = 0
failed = 0

test_cases = [
    ([1,2,3,0,0,0], 3, [4,5,6], 3, [1,2,3,4,5,6]),
    ([0,0,0], 0, [1,2,3], 3, [1,2,3]),
    ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6]),
    ([1,2,2,0,0,0,0], 3, [2,2,5,6], 4, [1,2,2,2,2,5,6]),
    ([1,1,1,0,0,0], 3, [1,1,1], 3, [1,1,1,1,1,1]),
    ([-3,-2,-1,0,0,0,0], 3, [0,2,3,4], 4, [-3,-2,-1,0,2,3,4]),
    ([2,0], 1, [1], 1, [1,2])

]

for nums1, m, nums2, n, expected in test_cases:
    result = sol.merge_sort(nums1, m, nums2, n)

    if nums1 == expected:
        print(f"Passed")
        passed += 1

    else:
        print(f"Failed -> got {nums1}, expected{expected}")
        failed += 1

print(f"\n {passed} passed, {failed} failed out of {len(test_cases)} tests")