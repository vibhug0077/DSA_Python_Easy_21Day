from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
def build_list(arr):
    dummy = ListNode(-1)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_array(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def main():
    l1 = build_list([1,2,4])
    print(l1.next.next.val)
    l2 = build_list([1,3,4])
    print(to_array(Solution().mergeTwoLists(l1, l2)))


if __name__ == "__main__":
    main()