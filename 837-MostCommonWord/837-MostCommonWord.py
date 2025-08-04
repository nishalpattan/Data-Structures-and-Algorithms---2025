# Last updated: 8/3/2025, 9:02:54 PM
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z0-9]", " ", paragraph)
        banned = set(banned)
        hash_map = dict()
        most_common_word = ""
        max_freq = 0
        for word in paragraph.split():
            if word.isalnum() and word not in banned:
                hash_map[word] = hash_map.get(word, 0) + 1
        print(hash_map)
        for word, freq in hash_map.items():
            if freq > max_freq:
                most_common_word = word
                max_freq = freq
        return most_common_word
        
        
        