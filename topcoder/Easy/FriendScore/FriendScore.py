
class FriendScore:
    
    def __init__(self):
        self.result = 0
        
    def highestScore(self, friends):
        
        friendsCnt = -1
        friendList = []
        
        for index,friend in enumerate(friends):
            
            friendList1 = set()
            for i,v in enumerate(friend):
                if v == "Y":
                    friendList1.add(i)
            
            friendList2 = set()
            for index, friend in enumerate(friendList1):

                for i,v in enumerate(friends[friend]):
                    if v == "Y":
                        friendList2.add(i)
                
            friendList = list(friendList1) + list(friendList2)
            if len(set(friendList)) > friendsCnt:
                friendsCnt = len(set(friendList)) - 1
            
            if friendsCnt == -1:
                friendsCnt = 0
                
            self.result = friendsCnt
            print(self.result)
            
        return self.result


friendScore = FriendScore()

friendScore.highestScore(("NNNNNNNNNNNNNNY", "NNNNNNNNNNNNNNN", "NNNNNNNYNNNNNNN", "NNNNNNNYNNNNNNY", "NNNNNNNNNNNNNNY", "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNYYNNNNNNNNNNN", "NNNNNYNNNNNYNNN", "NNNNNNNNNNNNNNY", "NNNNNNNNNNNNNNN", "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNNNNNNNNNNNNNN", "YNNYYNNNNYNNNNN"))

