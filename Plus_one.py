

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _c1 = ""
        holder = 0
        pair_list = []
        for index , z in enumerate((digits[::-1])):
            if index == 0:
                holder+=z
                continue
            _c1 = str(str(_c1)+"0");_c3 = str(str(z)+_c1)
            holder+=int(_c3)
        holder+=1
        for delta in str(holder):
            pair_list.append(int(delta))
        return pair_list
        


digits_1 = [1,2,3]

# [1,2,4]
digits_2 = [4,3,2,1]
# [4,3,2,2]
digits_3 = [9]
# [1,0]

digits_4 = [0,0,0]

Obj = Solution()
out = Obj.plusOne(digits_2)
print(f"Output: {out}")