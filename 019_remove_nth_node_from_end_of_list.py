# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head.next
        p = head
        if head == None or cur == None:
            return None
        i = 1
        flag = 0
        next_to_delete = 0
        while(cur):
            cur = cur.next
            if i == n:
                next_to_delete = 1
            if (i > n):
                flag = 1
                p = p.next
            i += 1
        if flag or next_to_delete:
            temp = p.next
            p.next = temp.next
            temp.next = None
        else:
            head = head.next
        return head


def list_to_node(x):
    head = ListNode(x[0])
    p = head
    for i in range(1,len(x)):
        p.next = ListNode(x[i])
        p = p.next
    return head


def node_to_list(head):
    x = []
    p = head
    i=0
    while p:
        x.append(p.val)
        p = p.next
        i+=1
    return x

if __name__ == '__main__':
    result = Solution().removeNthFromEnd(list_to_node([1, 2, 3]), 3)
    print(node_to_list(result))