
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        address_list = address.split(".")
        
        result = ""
        for index, number in enumerate(address_list):
            result += number
            if not index == len(address_list)-1:
                result += "[.]"
                
        return result


sol = Solution()
sol.defangIPaddr(address = "1.1.1.1")

