import csv
from APIController import APIController

def csvWriter_Game(season):
    client = APIController('nba', season)
    print('Initiated Controller')

    #Read stats and abbreviations from file
    statString, statList = getStats()
    
    #Create the header list and add it to a new file
    headers = ['game_id', 'team_id', 'player_id']
    headers.extend(statList)

    teamList = getTeams()

    with open('game_' + season + '.csv', 'w') as csvfile:
        file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        file.writerow(headers)

    for team in teamList:
        print('Making GET call for ' + team)
        gameJSON = client.getPlayerGamelogs(team=team,playerstats=statString)

        with open('game_' + season + '.csv', 'a') as csvfile:
            file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    
            for gamePlayer in gameJSON['playergamelogs']['gamelogs']:
                keys = [gamePlayer['game']['id'], gamePlayer['team']['ID'], gamePlayer['player']['ID']]
                row = keys
                for stat in statList:
                    row.append(gamePlayer['stats'][stat]['#text'])
                file.writerow(row)

        print('Write Complete for ' + team)    

#read the file of desired fields and put it in a list and string.
def getStats():
    statList = []
    statString = ''
    with open('desired_stats.csv', 'r') as statFile:
        f = csv.reader(statFile, delimiter=',', lineterminator='\n')
        for statRow in f:
            statString = statString + ',' + statRow[1]
            statList.append(statRow[0])

    #Trimming leading comma
    statString = statString[1:]
    return statString, statList

#read the file of teams and put it in a list.
def getTeams():
    teamList = []
    with open('TeamList.csv', 'r') as teamFile:
        f = csv.reader(teamFile, delimiter=',', lineterminator='\n')
        for teamRow in f:
            teamList.append(teamRow[0])
            
    return teamList
