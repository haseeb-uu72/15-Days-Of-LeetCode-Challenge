class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list to easily modify it
        s = list(s)
        
        # Loop through the string in steps of 2k
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters of the current 2k block
            s[i:i + k] = s[i:i + k][::-1]
        
        # Convert list back to string and return it
        return ''.join(s)
