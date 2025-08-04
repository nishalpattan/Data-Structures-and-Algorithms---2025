# Last updated: 8/3/2025, 9:02:13 PM
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = list()
        hash_set = set()
        
        for idx1, transaction1 in enumerate(transactions):
            name1, time1, amount1,city1 = transaction1.split(",")
            if int(amount1) > 1000:
                hash_set.add(transaction1)
            for idx2,transaction2 in enumerate(transactions[idx1 + 1:]):
                name2, time2, amount2,city2 = transaction2.split(",")
                if name1 == name2 and abs(int(time1) - int(time2)) <= 60 and city1 != city2:
                    if transaction2 not in hash_set:
                        hash_set.add(transaction2)
                    if transaction1 not in hash_set:
                        hash_set.add(transaction1)
        for invalid_transaction in hash_set:
            result.append(invalid_transaction)
        return result
