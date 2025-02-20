# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        # self.zero = []
        self.prefix = []

    def add(self, num: int) -> None:
        self.arr.append(num)
        if num != 0:
            if not self.prefix:
                self.prefix.append(num)
            else:
                self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix = []
            # self.zero.append(len(self.arr))


    def getProduct(self, k: int) -> int:
        if k > len(self.prefix):
            return 0
        elif k == len(self.prefix):
            return self.prefix[-1]
        else:
            return self.prefix[-1] // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)