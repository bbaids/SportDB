import csv
from APIController import APIController

def csvWriter_Roster(season, forDate):
    client = APIController('nba', season)
    print('Initiated Controller For ' + season)

    playerJSON = client.getPlayers(forDate)

    f = open('output.txt', 'w')
    f.write(str(playerJSON))
    f.close()
    
    with open('player_' + season + '.csv', 'w') as csvfile:
        file = csv.writer(csvfile, delimiter='c', lineterminator='\n')
        file.writerow(['playerkey','teamkey','datekey','lastname','firstname','position','height','weight','age','activeflag'])

    with open('player_' + season + '.csv', 'a') as csvfile:
        file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        for player in playerJSON['rosterplayers']['playerentry']:
            file.writerow([
                player['player']['ID']
                , player['team']['ID']
                , forDate
                , player['player']['LastName']
                , player['player']['FirstName']
                , player['player']['Position']
                , player['player']['Height']
                , player['player']['Weight']
                , player['player']['Age']
                , 1])

##Call that reads seasons and dates from nba_season
with open('nba_season.csv', 'r') as seasonFile:
    f = csv.reader(seasonFile, delimiter=',', lineterminator='\n')
    for seasonRow in f:
        if(seasonRow[0][-7:] == 'regular'):
            print('Begining Roster Write Process For ' + seasonRow[0])
            csvWriter_Roster(seasonRow[0], seasonRow[1])


