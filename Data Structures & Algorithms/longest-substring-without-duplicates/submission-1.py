class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        max_length = 0

        for r, c in enumerate(s):
            if s[r] in last_seen:
                l = max(l, last_seen[c] + 1)
            last_seen[s[r]] = r
            max_length = max(max_length, r - l + 1)
        return max_length
      

        