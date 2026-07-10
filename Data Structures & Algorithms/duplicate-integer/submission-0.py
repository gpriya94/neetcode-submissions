class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d_nums = {}
        for i in nums:           
            d_nums[i] = d_nums.get(i,0) + 1
            if d_nums[i] >= 2:
                return True
        return False

        