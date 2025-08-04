# Last updated: 8/3/2025, 9:02:58 PM
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = list()
        self.back_track(0, list(S), res)
        return res
    
    def back_track(self,start_idx, temp, res):
        res.append("".join(temp[:]))
        
        for i in range(start_idx, len(temp)):
            if temp[i].isalpha():
                if temp[i].isupper():
                    temp[i] = temp[i].lower()
                    self.back_track(i + 1, temp, res)
                    temp[i] = temp[i].upper()
                elif temp[i].islower():
                    temp[i] = temp[i].upper()
                    self.back_track(i+1, temp, res)
                    temp[i] = temp[i].lower()