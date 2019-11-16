from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1

        sortTasks = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        maxCount = sortTasks[0][1]

        res = (maxCount - 1) * (n + 1)
        for sortTask in sortTasks:
            if sortTask[1] == maxCount:
                res += 1

        if res < len(tasks): return len(tasks)
        else: return res