# Last updated: 8/3/2025, 9:02:06 PM
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # can use binary search
        # 1. sort the input products to recommend lexicographical words
        # 2. build prefix taking each char in search word and do binary search in products
             # where prefix is less than lexicographically in products set
        # 3. from binary search we know the left most index in products and check the product from there starts with the prefix build so far
        # 4 take atmost 3 words and store in the result

        #1.
        products.sort()
        result = []
        prefix = ""

        #2.
        for char in searchWord:
            prefix += char
            left, right = 0, len(products) - 1
            while left <= right:
                mid = (left + right) // 2
                if products[mid] < prefix:
                    left = mid + 1
                else:
                    right = mid - 1
            idx = left
            matches = []
            while idx < len(products) and len(matches) < 3:
                if products[idx][:len(prefix)] == prefix:
                    matches.append(products[idx])
                else:
                    break
                idx += 1
            result.append(matches)
        return result
