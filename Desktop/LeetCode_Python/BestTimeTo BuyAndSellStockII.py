class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        
        return max_profit

sol = Solution()

test_cases = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
    ([5], 0),
    ([1,2], 1),
    ([2,1], 0),
    ([3,3,3,3], 0),
    ([1,7,2,8,3,9], 18),
    ([5,1,5,1,5], 8),
    ([5,4,3,2,1,6], 5),
    ([0, 10000], 10000),
    ([1,2,1,2,1,2], 3),
    (list(range(1, 30001)), 29999),
    (list(range(30000, 0, -1)), 0)
]

passed = 0
failed = 0

for prices, expected in test_cases:
    result = sol.maxProfit(prices)
    if result == expected:
        print(f"Passed: {prices[:6]}{'...' if len(prices) > 6 else ''} → {result}")
        passed += 1
    else:
        print(f"Failed: {prices[:6]}{'...' if len(prices) > 6 else ''} → got {result}, expected {expected}")
        failed += 1