
import sys

class Solution:
    def __init__(self) -> None:
        # Should Output to true
        string_1 = "bbcc" # s
        string_2 = "ccbc" # t

        output = self.isAnagram(s=string_1, t=string_2)
        print(output)

    def isAnagram(self, s: str, t: str) -> bool:
        """
        - Loop through S(String_1)
          - For each string individually check if string is in string_2
          - If one string is false, return false
        return False
        """

        # Compare both counters
        counter_1 = {}
        counter_2 = {}

        for index in s: # String\
            if len(s) == len(t):    
                for string in index:
                    pass
                if string in t:
                    if string in counter_1:
                        counter_1[string] = counter_1[string]+1
                    else:
                        counter_1[string] = 1
                else:
                    return False
            else:
                return False
        for tee in t:
            if tee in counter_2:
                counter_2[tee] = counter_2[tee]+1
            else:
                counter_2[tee] = 1

        for x in counter_1:
            print(f"X: {x}")
            value = counter_1[x]
            if value == counter_2[x]:
                pass
            else:
                return False
        
        # Iterate through dictionary
        # use string from s to look through value for counter_2
           # if value isn't the same as the key/value pair from counter_1 return False
        # Return True

        #print(f"Counter 1: {counter_1}")
        #print(f"Counter 2: {counter_2}")
        return True


Solution()