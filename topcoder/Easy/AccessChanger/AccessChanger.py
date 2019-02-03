
class AccessChanger:
    def __init__(self):
        self.result = []
        
    def convert(self,program):
        cnt=program.count('"')
        
        for i,val in enumerate(program):
            barrier = val.find("//")

            if val.find("->")>-1 and val.find("//")>0:
                half1 = val[:barrier].replace("->",".")
                half2 = val[barrier:]
                val = half1 + half2
                
            else : 
                val = val.replace("->",".")
            
            self.result.append(val)
            print(tuple(self.result))

        return tuple(self.result)



ac = AccessChanger()
ac.convert(tuple({"->-> // two successive arrows ->->"}))
