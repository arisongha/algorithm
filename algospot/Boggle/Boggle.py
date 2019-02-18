
class Boggle:
    def __init__(self):
        self.dy = [0,1,1,1,0,-1,-1,-1]
        self.dx = [-1,-1,0,1,1,1,0,-1]
        self.board = [["U","R","L","P","M"],
                      ["X","P","R","E","T"],
                      ["G","I","A","E","T"],
                      ["X","T","N","Z","Y"],
                      ["X","O","Q","R","S"]]
    
    def hasWord(self, y: 'int', x: 'int', word: 'str') -> 'bool':
        
        if not (0<=x<=4 and 0<=y<=4):
            return False
        if not self.board[y][x] == word[0]:
            return False
        if len(word) == 1:
            return True
        
        word = word[1:len(word)]
        
        for i in range(0,8):
            nexty = y + self.dy[i]
            nextx = x + self.dx[i]
            
            if self.hasWord(nexty, nextx, word):
                return True
        
        return False


sol = Boggle()
sol.hasWord(1,2,"RPEAT")

