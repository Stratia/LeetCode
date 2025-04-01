
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Return amount of unique items, List
        # Issue: Modify the nums array
        new_nums = []
        for a in nums:
            if a in new_nums:
                continue
            else:
                new_nums.append(a)
        nums = new_nums
        k = len(new_nums)
        return int(k), new_nums
        
list_1 = [1,1,2]
list_2 = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
out = obj.removeDuplicates(list_1)

print(out)