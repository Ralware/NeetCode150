class Solution:
    def maxProfit(self, Prices: List[int]) -> int:
        Min = Prices[0]
        MaxDiff = 0
        for Index in range(len(Prices)):
            if Prices[Index] < Min:
                Min = Prices[Index]

            Diff = Prices[Index] - Min

            if Diff > MaxDiff:
                MaxDiff = Diff

        return MaxDiff