class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        pairs = []
        for word in strs:
         sorted_word = "".join(sorted(word))
         pairs.append((sorted_word, word))   
        pairs.sort(key=lambda x: x[0])
        
        result = []
        current_group = [pairs[0][1]]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] == pairs[i-1][0]:
                current_group.append(pairs[i][1])
            else:
                result.append(current_group)
                current_group = [pairs[i][1]]
        result.append(current_group)
        return result
        