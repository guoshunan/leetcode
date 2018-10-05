class Solution:
    def twoSum_my(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            first_num=nums[i]
            second_num=target-first_num
            if second_num in nums and nums.index(second_num)!=i:
                return [i,nums.index(second_num)]
            else:
                continue
        return 'No Solution'
    
    def twoSum(self, nums, target):
        collected = {}
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in collected:
                return [collected[diff], idx]
            collected[val] = idx
        