import csv
from APIController import APIController

def getStats(season, fordate):

        client = APIController('nba', season)

        print('Initiated Controller')

        seasonJSON = client.getCurrentSeason(fordate)

        print('Completed GET')

        statAbbreviation = []
        statName = []
        for stat in seasonJSON['currentseason']['season'][0]['supportedPlayerStats']['playerStat']:
                statistic = stat['abbreviation']
                if(not (statistic.endswith('/G') or statistic.endswith('%'))):
                        statAbbreviation.append(stat['abbreviation'])
                        statName.append(stat['name'].replace(" ", "_"))
        
        with open('stats_' + season + '.csv', 'w') as csvfile:
                file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                for i in range(len(statName)):
                        file.writerow([statName[i], statAbbreviation[i]])

with open('nba_season.csv', 'r') as csvfile:
        file = csv.reader(csvfile, delimiter=',', lineterminator='\n')
        for season in file:
                getStats(season[0], season[1])
