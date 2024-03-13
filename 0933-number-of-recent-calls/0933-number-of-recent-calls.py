class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.List = []
    def ping(self, t: int) -> int:
        if t <= 3000 or  (self.List and t - self.List[0] <= 3000):
            self.counter += 1
            self.List.append(t)
        
        else:
            
            while self.List and  t - self.List[0] > 3000:
                self.List.pop(0)
                
            self.List.append(t)
            self.counter = len(self.List)
        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)