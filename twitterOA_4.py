def isPossible(calCounts, requiredCals):
    # Write your code here
    size = len(calCounts)
    if size == 0:
        return False
    calCounts.sort()

    def DFS(calCounts, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            if calCounts[index] > residue:
                break
            if index > start and calCounts[index - 1] == calCounts[index]:
                continue
            path.append(calCounts[index])
            DFS(calCounts, size, index + 1, path, residue - calCounts[index], res)
            path.pop()
    res = []
    DFS(calCounts, size, 0, [], requiredCals, res)
    if len(res) == 0: return False
    else: return True
