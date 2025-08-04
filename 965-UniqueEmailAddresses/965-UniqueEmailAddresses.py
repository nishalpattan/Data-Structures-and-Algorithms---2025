# Last updated: 8/3/2025, 9:02:40 PM
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        prev_email = ""
        count = 0
        for idx,email in enumerate(emails):
            email_split = email.split("@")
            local_name, domain_name = email_split[0], email_split[1]
            local_name_split = local_name.split("+")[0]
            local_name_split = local_name_split.split(".")
            local_name = "".join(local_name_split)
            email = local_name + "@" + domain_name
            emails[idx] = email
        return len(set(emails))
        