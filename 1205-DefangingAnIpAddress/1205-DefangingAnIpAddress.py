# Last updated: 8/3/2025, 9:02:20 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")