# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            name, domain = email.split('@')
            if name.find('+') != -1:
                name = name[:name.find('+')].replace('.', '')
            else:
                name = name.replace('.', '')
            email_set.add(name + '@' + domain)
        return len(email_set)

if __name__ == '__main__':
    solution = Solution()
    input = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    res = solution.numUniqueEmails(input)
    print(res)