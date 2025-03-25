


from typing import List
from collections import defaultdict


"""
Given a list of words, group them by their unique set of characters (ignoring order and duplicates). 
Words with the same set of characters should be grouped together. 
Return the grouped words as a list of lists.

Summary:
Basically group all words with the same characters
"""

"""
Hint:
Instead of sorting the word, try using set() 
to get the unique characters, and 
convert that set into a string key.
"""


"""
Iterates through list:
 - Puts word in set for only unique character
 - Converts letters from set into a string
 - The converted letter is added a key with the 
   value being the word it was previously
 Visual:
 abcc --> abc --> Correct = [abc] = abcc
 bca --> abc --> Correct = [abc] = bca, abcc
"""
class Solution:
    def group_by_common(self, strs: List[str]) -> List[List[str]]: # Out = Sublist
        Correct = {} 
        mo_par = []

        for Original_String in strs: # Iterates through list
            a = set(Original_String) # Puts letters through set geting rid of repeated characters
            joined_string = "" # Will contain all unique characters (No Repeated Ones)

            for z in a: # Iterates through set
                joined_string+="".join(z) # Concatenates each letter in set to final string

            Sorted_String = ''.join(sorted(joined_string))
            Correct.setdefault(Sorted_String, []).append(Original_String)
        for c in Correct:
            list_pairings = Correct[c]
            mo_par.append(list_pairings)
        print(mo_par)

io = ["abc", "bca", "cab", "foo", "ofo", "bar", "bra"]
#  [["abc", "bca", "cab"], ["foo", "ofo"], ["bar", "bra"]]

io_2 = ["abcc", "bca"]

io_3 = ["", "", ""]

obj = Solution()
output = obj.group_by_common(io)

print(output)

