class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            hashmap[sorted_string].append(s)
        return list(hashmap.values())

        
        