from typing import List
def check_log_history(events: List[str]):
    if len(events) == 0: return 0
    # A stack to meet the acquire and release function. A set to check whether there is repeated number.
    stack = []
    visited = set()

    for i in range(len(events)):
        method, value = events[i].split(" ")

        if method == "ACQUIRE":
            # Repeated acquire number will output N+1.
            # Else push the value into stack and the set.
            if value in visited: return i + 1
            visited.add(value)
            stack.append(value)
        elif method == "RELEASE":
            # If number released is on top of stack, pop and remove if from the set.
            # Else return N+1.
            if stack != [] and stack[-1] == value:
                visited.remove(stack.pop())
            else:
                return i + 1
    return 0 if stack == [] else len(events) + 1