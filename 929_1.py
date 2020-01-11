from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        count = 0

        for email in emails:
            name, domain = email.split("@")
            name = name.replace(".", "")
            if name.find("+") != -1:
                name = name[:name.find("+")]
            if name + "@" + domain not in res:
                res.append(name + "@" + domain)
                count += 1
        return count