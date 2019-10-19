# Time: O(kn), k is the number of linked lists. 最终的每个结点都经过O(K)的比较
# Space: O(n)
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Compare one by one
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        result = ListNode(0)
        r_p = result
        length = len(lists)
        i, j = 0, 0
        while j < length:  # 删除所有None的结点
            if lists[j] is None:
                del lists[j]
                j -= 1
                length -= 1
            j += 1
        while length != 0:
            cur_min_val = lists[0].val
            cur_min = 0
            for i in range(length):
                p = lists[i]
                if p.val < cur_min_val:
                    cur_min = i
                    cur_min_val = p.val
            new_node = ListNode(cur_min_val)
            r_p.next = new_node
            r_p = r_p.next
            lists[cur_min] = lists[cur_min].next
            if lists[cur_min] is None:  # 删除所有None的结点
                del lists[cur_min]
                length -= 1

        return result.next


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
    result = Solution().mergeKLists([list_to_node([2]), list_to_node(None), list_to_node([1,2,3])])
    print(node_to_list(result))