class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # every valyue inside this dict will be a list
        res = defaultdict(list) # special hash map--> tries to create an empty list when appending a key that doesnt exist. Prevents extra if/else chcks inside the loop

        for word in strs:
            key = frozenset(Counter(word).items())
            res[key].append(word)

        return list(res.values())