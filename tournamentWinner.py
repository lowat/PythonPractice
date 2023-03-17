def tournamentWinner(competitions, results):
    scoreboard = {}
    leadingTeam = ""
    highScore = 0
    for idx, competition in enumerate(competitions):
        currentCompetitionWinIdx = 0 if results[idx] == 1 else 1
        currentCompetitionWinningTeam = competition[currentCompetitionWinIdx]
        currentWinningTeamScore = scoreboard.get(currentCompetitionWinningTeam , 0) + 3
        scoreboard.update({currentCompetitionWinningTeam: currentWinningTeamScore})
        if currentWinningTeamScore > highScore:
            leadingTeam = currentCompetitionWinningTeam
            highScore = currentWinningTeamScore
    return leadingTeam
        