class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(count)
        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] += 1

            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
        
        start, end = res

        return s[start : end + 1] if res_len != float("inf") else ""





        



            

        

        
        