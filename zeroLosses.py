class Solution(object):
    def findWinners(self, matches):
        wonAll = []
        lostOne = []
        playerMap = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner in playerMap:
                playerMap[winner][0] = playerMap[winner][0] + 1
            else:
                playerMap[winner] = [1,0]
            if loser in playerMap:
                playerMap[loser][1] = playerMap[loser][1] + 1
            else:
                playerMap[loser] = [0,1]
        for player, record in playerMap.items():
            if record[1] == 0:
                wonAll.append(player)
            elif record[1] == 1:
                lostOne.append(player)
        wonAll.sort()
        lostOne.sort()
        return [wonAll, lostOne]
            
        
        
        