# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        p1,p2=l1,l2
        p = ListNode(0)
        re = p
        while p1!=None and p2 != None:
            if p1.val>p2.val:
                p.next = p2
                p=p.next
                p2=p2.next
            elif p1.val < p2.val:
                p.next = p1
                p=p.next
                p1=p1.next
            else:
                p.next = p1
                p1=p1.next
                p = p.next
                p.next = p2
                p2=p2.next
                p = p.next

        if p1 == None:
            p.next=p2
        if p2 == None:
            p.next=p1
        return re.next


def list_to_node(x):
    if x == None:
        return None
    head = ListNode(x[0])
    p = head
    for i in range(1,len(x)):
        p.next = ListNode(x[i])
        p = p.next
    return head


def node_to_list(head):
    if head == None:
        return None
    x = []
    p = head
    i=0
    while p:
        x.append(p.val)
        p = p.next
        i+=1
    return x

if __name__ == '__main__':
    # result = Solution().mergeTwoLists(list_to_node(None), list_to_node([1.5, 2, 3]))
    result = Solution().mergeTwoLists(list_to_node([2]), list_to_node([1]))
    print(node_to_list(result))