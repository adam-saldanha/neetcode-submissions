class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        hashmap = {}

        for string in strs:
            count = tuple(string.count(char) for char in alphabet)
            if count not in hashmap:
                hashmap[count] = [string]
            else:
                hashmap[count].append(string)

        
        res = []
        for anagram in hashmap:
            res.append(hashmap[anagram])
        return res


        