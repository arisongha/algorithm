class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = eval('*'.join([i for i in str(n)]))
        sum_ = eval('+'.join([i for i in str(n)]))
        return product - sum_
