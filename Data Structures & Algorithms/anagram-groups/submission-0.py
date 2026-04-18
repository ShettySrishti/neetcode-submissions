class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # every valyue inside this dict will be a list
        res = defaultdict(list) # special hash map--> tries to create an empty list when appending a key that doesnt exist. Prevents extra if/else chcks inside the loop

        for word in strs:
            cnt = [0]*26 # creating freq array for 26 lowercase letters
            # populating freq array
            for char in word:
                # calculatng idx 0-25 using ASCII values
                idx = ord(char)-ord('a')
                cnt[idx] +=1

            res[tuple(cnt)].append(word)

        return list(res.values())

