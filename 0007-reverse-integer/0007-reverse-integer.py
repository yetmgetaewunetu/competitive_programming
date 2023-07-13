class Solution:
    def reverse(self, x: int) -> int:
        string = str(x).strip()
        List = []
        for i in string:
            List.append(i)
        ans = []
        print(List)
        for i in range(len(List)):
            ans.append(List.pop())

        if '-' in ans:
            num = '-'
            ans.remove('-')

            for i in ans:

                num += i
            if int(num) in range((-2) ** 31, 2 ** 31):
                return int(num)
            else:
                return 0
        else:
            num = ''
            for i in ans:
                num += i
            if int(num) in range((-2) ** 31, 2 ** 31):
                return int(num)
            else:
                return 0