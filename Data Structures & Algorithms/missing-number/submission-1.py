class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = sorted(nums)

        for i in range(len(nums)):
            if res[i] != i:
                return i

        return len(nums)




