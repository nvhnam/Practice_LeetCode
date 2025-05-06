from collections import deque

class ImplementStackQueue:
    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.appendleft(x)

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if len(self.q1) > 0:
            return False
        else: return True