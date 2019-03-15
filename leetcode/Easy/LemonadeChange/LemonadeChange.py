
class Solution:
    def lemonadeChange(self, bills: 'List[int]') -> bool:
        collect = []
        
        for index, bill in enumerate(bills):
            
            if index == 0:
                if not bill == 5:
                    return False
            
            collect.append(bill)
            
            try:
                if bill == 10:
                    collect.pop(collect.index(5))

                elif bill == 20:
                    if 10 in collect:
                        collect.pop(collect.index(5))
                        collect.pop(collect.index(10))
                    else:
                        collect.pop(collect.index(5))
                        collect.pop(collect.index(5))
                        collect.pop(collect.index(5))
                    
            except:
                return False
        
        return True            


sol = Solution()
sol.lemonadeChange([5,5,5,10,5,5,10,20,20,20])

