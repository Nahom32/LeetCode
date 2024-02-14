class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        nums = []
        while neg != [] and pos != []:
            nums.append(pos.pop(0))
            nums.append(neg.pop(0))
        return nums
     
        
        
        