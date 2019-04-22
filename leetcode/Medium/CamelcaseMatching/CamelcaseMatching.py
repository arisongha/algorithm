
class Solution:
    def camelMatch(self, queries: 'List[str]', pattern: str) -> 'List[bool]':
        
        result = []
        for querie in queries:
            camel = ""
            for i,v in enumerate(querie):
                if v.isupper():
                    camel += v
                
            result.append(camel)
        
        returnBool = []
        for camel in result:
            if camel == pattern:
                returnBool.append(True)
            else:
                returnBool.append(False)
                
        return returnBool
                


sol = Solution()
sol.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB")

