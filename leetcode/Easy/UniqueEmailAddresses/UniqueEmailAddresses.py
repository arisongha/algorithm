
class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> int:
        filteredEmail = []
        for email in emails:
            plusIndex = email.find("+")
            atIndex = email.find("@")
            newEmail = ""
            for i,v in enumerate(email):
                if plusIndex == -1:
                    if i < atIndex:
                        if v == ".":
                            newEmail += ""
                        else:
                            newEmail += v
                    else:
                        newEmail += v
                else:

                    if plusIndex <= i < atIndex:
                        newEmail += ""
                    else:
                        if i < atIndex:
                            if v == ".":
                                newEmail += ""
                            else:
                                newEmail += v
                        else:
                            newEmail += v


            filteredEmail.append(newEmail)
            
        dic = dict()
        for i,v in enumerate(filteredEmail):
            dic[v] = dic.get(v, 0) + 1
            
        return len(dic)
                


sol = Solution()
sol.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"])

