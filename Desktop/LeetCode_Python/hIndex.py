class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        
        return h
    
sol = Solution()

test_cases = [
    ([3,0,6,1,5], 3),
    ([1,3,1], 1),

    ([0], 0),
    ([1], 1),
    ([100], 1),

    ([0,0,0,0], 0),

    ([3,3,3,3], 3),
    ([5,5,5,5,5], 5),

    ([10,10,10,10], 4),

    ([1,2,3,4,5], 3),
    ([5,4,3,2,1], 3),

    ([0,0,0,100], 1),

    ([100]*100, 100),

    ([0,0,0,0,5], 1),

    ([6,5,3,1,0], 3)
    ]

passed = 0
failed = 0

for citations, expected in test_cases:
    result = sol.hIndex(citations[:])
    if result == expected:
        print(f"Passed: {citations} -> result")
        passed += 1
        
    else:
        print(f"Failed: {citations} -> got {result}, expected {expected}")
        failed += 1
    
print(f"\n{passed} passed, {failed} failed out of {len(test_cases)} tests")

