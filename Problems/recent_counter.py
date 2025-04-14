from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.counter += 1

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.counter -= 1

        return self.counter