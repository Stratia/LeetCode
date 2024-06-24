class Solution:
    def __init__(self) -> None:
         input = [1,2,3,4]
         self.hasDuplicate(nums=input)

    # Determines if any duplicate numbers in list
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        - Iterate through list 
          - When iterating, add a counter for each number in dict
            - Example: {3:1} (Number/Counter)

          - If counter higher than 1 return True
          - If counter is not higher than 1 return Fals 
        """
        counter = {}
        for i in nums:
            # Checks if number is already in counter dict, if so adds 1 to the value
            if i in counter:
                counter[i] = counter[i]+1
                print(f"DUPLICATE FOUND: {i}")
                return True
            counter[i] = 1
        return False
        print(counter)
    
    

Solution()