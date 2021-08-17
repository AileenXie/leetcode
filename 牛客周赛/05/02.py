class Solution:
    def turn(self , s , k ):
        # write code here
        if k==0: return 0
        if not s: return 0
        ans = 0
        for i,c in enumerate(s):
            if i<len(s)-2 and ord(c)<ord(s[i+2]):
                ans+=1
        return ans

if __name__ =="__main__":
    # s,k="cbexa",2
    s,k="abcdefg",2
    print(Solution().turn(s,k))