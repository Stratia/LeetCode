
from typing import Optional
import sys

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list= [] 
        bn = []
        hn = []
        ln = []
        print(list1.val())
        sys.exit()
        p_1 = 0 ;p_2 = 0
        for count, index in enumerate(range(0, 5)):
            print("------")
            p1 = list1[p_1]
            p2 = list2[p_2]
            if not bn: 
                if p1 < p2:
                    merged_list.extend([p1, p2])
                    bn.append(p2)
                else:
                    merged_list.extend([p2, p1])
                    bn.append(p1)
            else:
                """
                If lowest number is smaller than previous number, it will be placed behind
                stacks position, the highest number will by default be placed ahead of stacks new 
                position
                """
                if p1 < p2:
                    ln.append(p1);hn.append(p2)
                else:
                    ln.append(p2);hn.append(p1)
                print(f"HARA: P1: {p1} | P2: {p2}")
                if ln[0] <= bn[0]: # If Previous number was higher than current lowest number
                    merged_list[count] = ln[0]
                    merged_list.extend([bn[0], hn[0]])
                else: # if Previous number is lower than current lowest number
                    merged_list[count] = bn[0]
                    merged_list.extend([ln[0],hn[0]])

                ln.pop()
                hn.pop()
                bn.pop()
        
            print("Merged List: ", merged_list)    
            p_1+=1
            p_2+=1

list1 = [1 ,2, 4, 5, 6, 7]
list2 = [1 ,3 ,4, 5, 8, 10]

obj = Solution()
prime = obj.mergeTwoLists(list1, list2)
print(prime)

