
import sys

"""
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

valid_cache = []

class Solution: # Returns boolean
    # Parenthese must be closed
    # All parenthese must be closed
    """
    This is a sort of 'bounce' algoritiom, not fast nor perfect but it gets the 
    job done
    Code Logic:
    1: In first for-loop, the loops looks for a "("
    2: Once first parenthese is found, create a seperate for-loop to loop for a corresponding closing bracket
       - This will happen for each ")" instance
    ")"
    """
    
    def isValid(self, s: str) -> bool:
        # Todo: Now do checking for closing brackets, this is going to get messy
        for count, index in enumerate(s):
            if index == "(":
                cache_pair = None
                print(f"'(' Found: {index}")

                for par in s[count:]:
                    if par == ")":
                        valid_cache.append(True)
                        print("Valid Pair Found")
                        cache_pair = True

                if cache_pair == None:
                    valid_cache.append(False);cache_pair = None

            if index == ")": # Same algor
                cache_pair = None
                print(f"')' Found: {index}")
                for close in s[:count]:
                    if close == "(":
                        valid_cache.append(True)
                        cache_pair = True
                if cache_pair == True:
                    pass
                else:
                    valid_cache.append(False);cache_pair = None
            else:
                print(index)
        print(f"Valid Cache: {valid_cache}")

        if False in valid_cache:
            return False
        else:
            return True

s = "()"
s2 = "(*FVJ$)"
s3 = "(CH(#))F#)$(($)()$()))"
s4 = "(]"
obj = Solution()
valid = obj.isValid
value = valid(s3)

print("Output: ",value)