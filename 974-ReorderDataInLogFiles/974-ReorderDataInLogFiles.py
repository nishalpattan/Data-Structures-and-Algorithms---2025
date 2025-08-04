# Last updated: 8/3/2025, 9:02:37 PM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()
        for log in logs:
            if log.split()[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs = sorted(letter_logs, key=lambda x : x.split()[0])  
        letter_logs = sorted(letter_logs, key=lambda x : x.split()[1:])  
        logs.clear()
        logs += letter_logs
        logs += digit_logs
        return logs