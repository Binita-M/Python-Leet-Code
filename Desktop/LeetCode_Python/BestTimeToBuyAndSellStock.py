class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            elif price - min_price > max_profit:
                max_profit = price - min_price
            
        return max_profit

sol = Solution()

test_cases = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([5], 0),
    ([1,2], 1),
    ([2,1], 0),
    ([3,3,3,3], 0),
    ([1,2,3,4,5], 4),
    ([2,4,1,7,3,1], 6),
    ([3,1,10,2,8], 9),
    ([5,4,3,2,1,10], 9),
    ([10,1,2], 1),
    (list(range(1000, 0, -1)), 0),
    (list(range(1, 10001)), 9999),
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

print(f"\n{passed} passed, {failed} failed out of {len(test_cases)} tests")