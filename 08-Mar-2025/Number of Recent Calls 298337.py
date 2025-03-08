# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.cur = 0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.cur += 1
        while self.queue and t - self.queue[0] > 3000:
            self.queue.popleft()
            self.cur -=1
        return self.cur


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)