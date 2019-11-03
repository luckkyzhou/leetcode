class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    sum = 0

    def getImportance (self, employees, id):
        hashmap = {}
        for employee in employees:
            hashmap[employee.id] = employee

        def DFS (id):
            if hashmap[id].subordinates == []:
                self.sum += hashmap[id].importance
                return
            for sub in hashmap[id].subordinates:
                DFS(sub)
            self.sum += hashmap[id].importance
            return

        DFS(id)
        return self.sum
