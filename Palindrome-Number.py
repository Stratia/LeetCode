from typing import List #  Imports to allow typing, allowing to specifiy what variables are wanted

# Given an integer x, return true if x is a palindrome, and false otherwise.
"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution: #  Creats a class object to contain the Solutition
    def isPalindrome(self, x: int) -> bool: #  Function accepts int and excepts a boolean (True/False) output/return
        
        # This is because a negative number will never be a Palindrome
        # Example: -121 | 121-, because of the negative symbole it will never read the same

        if x < 0: #  If x is less than zero | As the monster wants to eat whatever is biggest | Example: 121 < 0 (True) | Example: -121 (False)
            return False 
            
        abs_x = abs(x) # Returns absolute value of a int, removing negative or any numerical symbols

        reversed_x = int(str(abs_x)[::-1]) #  Reverses X using string splicing, by using [::-1] which starts from the very end of a string

        if reversed_x == x: #  Checks if reversed is same as abs
            return True #  Returns as True if Palindrome
            
        else: #  If the reversed int isn't the same as the original X value
            return False #  Returns False if not Palindrome
