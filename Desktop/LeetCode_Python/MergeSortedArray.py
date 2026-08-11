def merge(nums1, m, nums2, n):
    p1, p2, r = (m-1, n-1, m+n-1)

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[r] = nums1[p1]
            p1 -= 1
    
        else:
            nums1[r] = nums2[p2]
            p2 -= 1
    
        r -= 1

def test_merge():
    tests_passed = 0
    tests_failed = 0

    test_cases = [
        # (nums1, m, nums2, n, expected, description)

        # Basic cases
        ([1,2,3,0,0,0], 3, [2,5,6],  3, [1,2,2,3,5,6], "Basic merge"),
        ([1],           1, [],        0, [1],            "nums2 is empty"),
        ([0],           0, [1],       1, [1],            "nums1 is empty"),

        # Edge cases
        ([0,0,0],       0, [1,2,3],   3, [1,2,3],        "All elements from nums2"),
        ([1,2,3,0,0,0], 3, [4,5,6],   3, [1,2,3,4,5,6],  "nums1 all smaller"),
        ([4,5,6,0,0,0], 3, [1,2,3],   3, [1,2,3,4,5,6],  "nums2 all smaller"),

        # Duplicates
        ([1,2,2,0,0,0], 3, [2,2,3],   3, [1,2,2,2,2,3],  "Duplicate elements"),
        ([1,1,1,0,0,0], 3, [1,1,1],   3, [1,1,1,1,1,1],  "All same elements"),

        # Negative numbers
        ([-3,-1,0,0,0], 2, [-2,1,2],  3, [-3,-2,-1,1,2], "Negative numbers"),

        # Single elements
        ([2,0],         1, [1],        1, [1,2],           "Single elements"),
    ]

    for nums1, m, nums2, n, expected, description in test_cases:
        merge(nums1, m, nums2, n)

        if nums1 == expected:
            print(f" PASSED | {description}")
            tests_passed += 1
        else:
            print(f" FAILED | {description}")
            print(f"         Expected : {expected}")
            print(f"         Got      : {nums1}")
            tests_failed += 1

    print(f"\n Results: {tests_passed} passed, {tests_failed} failed out of {len(test_cases)} tests")

test_merge()


