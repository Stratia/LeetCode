
import sys

"""
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

valid_cache = []

class Solution(object):

    def isValid(self, s):
        """
        Paradign Equalization Metric Algoritiom:
         Operating Procedures: 
           - It will iterate through the given string, when encountering an opening bracket it will
             store it in the stack (cache), when encountering a closing bracket, it will check the last 
             entered value within the stack; If this value doesn't corresponding to the current closing bracket
             it will return False. If it does, stack will be deleted. 

             If stack is empty return True
        """
        stack = [] # Cache to store last encountered opening bracket
        for algor in s: # Iterates through string to find brackets
            if algor in '([{': # If detects string that is an opening bracket
                stack.append(algor) # Will append it to stack for reference when closing bracket is found
            else: # Closing Bracket
                if not stack: # If stack is empty, will return False because a corresponding closing bracket doesn't exist or hasn't been encoutered
                    return False 
                else: # If stack is filled | Basically, if an opening bracket has been encountered
                    # All of these check if the last encountereed opening bracket corresponds with the current closing bracket
                    if stack[-1] == "(" and algor == ")": 
                        stack.pop()
                    elif stack[-1] == "[" and algor == "]":
                        stack.pop()
                    elif stack[-1] == "{" and algor == "}":
                        stack.pop()
                    else: # Returns false because last encountered opening bracket and current closing bracket don't match
                        return False
        # If everything is fine stack will return True, since everything correspondings, if things didn't it wouldn't
        # Have gotten to this line of code anyways
        if not stack:
            return True
        else:
            return False
   

s5 = "(])" # False

obj = Solution()
valid = obj.isValid
value = valid(s5)

print("Output: ",value)