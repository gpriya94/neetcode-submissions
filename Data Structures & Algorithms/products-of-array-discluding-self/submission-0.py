class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_list = [1] * n
        prefix = 1
        for i in range(n):
            prefix_list[i] = prefix
            prefix = prefix * nums[i]
        sufix_list = [1] * n
        sufix = 1
        for i in range(n-1,-1,-1):
            sufix_list[i] = sufix
            sufix = sufix * nums[i]
        for i in range(n):
            result[i] = prefix_list[i] * sufix_list[i]
        return result