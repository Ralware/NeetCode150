class Solution:
    def longestConsecutive(self, Nums: List[int]) -> int:
        Nums = sorted(set(Nums))

        Count = 0
        MaxCount = 0

        for Index in range(len(Nums) - 1):

            if Nums[Index + 1] - Nums[Index] == 1:
                Count += 1
            else:
                MaxCount = max(Count, MaxCount)
                Count = 0

        MaxCount = max(Count, MaxCount)

        return MaxCount + 1 if Nums else 0