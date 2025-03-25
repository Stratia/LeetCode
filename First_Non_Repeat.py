
"""
Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.
""" 
"""
- Create Counter of each letter
  - {
  L: [0, 0]
  e: 2
  T: [0, 3]
  C: 0
  o: 0
  d: 0
  }
  Counter: Mechanism
  -
  - First letter with counter less than 0 gets it
    index returns
"""
class Solution:
    def firstUniqChar(self, s: str) -> int: 
        """
        iterate through string and create a dictionary, each 
        time the letter is iterated through, the counter will go up 
        by 1 (Starting at 0)

        Afterwards, a for-loop will iterate through all keys,
        the first one with a counter of 0 will get its index returned
        """
        _Lookip = list(s);counter_dic = {}
        test = {'l': ['a', 0], 'e': ['a', 7], 't': ['a', 3], 'c': ['a', 4], 'o': ['a', 5], 'd': ['a', 6]}
        for index, a in enumerate(_Lookip):
            if a in counter_dic.keys():
                av = counter_dic[a][0]=+1
                counter_dic[a] = [av, index]
            else:
                print(f"No Key for {a} adding")
                counter_dic[a] = [0, index]

        print(counter_dic)
        for index, c in enumerate(counter_dic):
            value = counter_dic[c[0]]
            #print(f"Value: {value[0]}")
            if value[0] == 0:
                print(f"First Unique Char is: {c}, | Index: {counter_dic[c][0]}")
                return counter_dic[c][1]
        return -1

string_1 = "leetcode" # 0 (L)
string_2 = "loveleetcode" # 2 (V)
string_3 = "fregtehbwrgfevwefrgtewbrwbetgsdgrterL"
string_4 = "aabb"
string_5 = "dddccdbba"

Sol_Obj = Solution()
output = Sol_Obj.firstUniqChar(string_3)
print(f"Out: {output}")