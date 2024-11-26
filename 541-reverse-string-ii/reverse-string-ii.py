class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse1(s, k):
            if len(s)<k:
                return s[::-1]
            if len(s)>=k and len(s)<=2*k:
                s1 = s[:k]; s2 = s[k:]
                s1 = list(s1)
                i = 0; j = len(s1)-1
                while(i<j):
                    temp = s1[i]; s1[i] = s1[j]; s1[j] = temp
                    i+=1; j-=1
                s1 = ''.join(s1)
                return s1+s2
            else:
                return reverse1(s[:(2*k)], k) + reverse1(s[(2*k):], k)
        s = reverse1(s, k)
        return s