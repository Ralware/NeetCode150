class Solution:
    def twoSum(self, Nums: List[int], Target: int) -> List[int]:

        Data = {}

        for Index in range(len(Nums)):

            Difference = Target - Nums[Index]

            if Difference in Data:
                return [Data[Difference] + 1, Index + 1]

            Data[Nums[Index]] = Index

        return []

        