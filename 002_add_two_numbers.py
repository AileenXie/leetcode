# Time: O(n)
# Space: O(n)
#
# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        r = ListNode(0)
        cur = r
        residue = 0
        while p1 is not None or p2 is not None:
            if p1 is None:
                a = 0
            else:
                a = p1.val
                p1 = p1.next
            if p2 is None:
                b = 0
            else:
                b = p2.val
                p2 = p2.next
            cur.val = (a + b + residue) % 10
            residue = (a + b + residue) // 10
            new_node = ListNode(0)
            cur.next = new_node
            p = cur
            cur = new_node

        if residue != 0:
            cur.val = residue
        else:
            p.next = None
        return r


if __name__ == '__main__':
    m, m.next, m.next.next = ListNode(9), ListNode(9), ListNode(3)
    n, n.next, n.next.next = ListNode(1), ListNode(0), ListNode(4)
    result = Solution().addTwoNumbers(m, n)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
