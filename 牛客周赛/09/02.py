
class TreeNode:
    def __init__(self,val=0):
        self.val = val
        self.left=None
        self.right=None

class Solution:
    def solve(self , n , pre , suf ):
        # write code here
        if not n: return []
        root = TreeNode(pre[0])
        st = [root]
        at=0
        for i in range(1,n):
            cur = TreeNode(pre[i])
            if st[-1].left==None:
                st[-1].left=cur
            else:
                st[-1].right=cur
            st.append(cur)
            while st and at != n and suf[at] == st[-1].val:
                at +=1
                st.pop()
        self.ans = []

        def inorder(node):
            if not node: return
            inorder(node.left)
            self.ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return self.ans

n,pre,suf=5,[3,2,1,4,5],[1,5,4,2,3]
n,pre,suf=0,[],[]
n,pre,suf=5,[1,2,3,4,5],[5,4,3,2,1]
print(Solution().solve(n,pre,suf))


