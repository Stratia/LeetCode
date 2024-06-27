
class Solution:
    def __init__(self) -> None:
        list_1 = [-1,-2,-3,-4,-5] # 2 4
        target_number = -8

        self.twoSum(nums=list_1, target=target_number)

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index_main, x in enumerate(nums):
            for index_second, add in enumerate(nums):
                if index_second == index_main:
                    continue
                else:
                    if x+add == target:
                        indices = [index_main, index_second]
                        print(indices);return indices
                    else:
                        continue

Solution()