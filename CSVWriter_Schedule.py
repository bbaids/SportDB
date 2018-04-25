import csv
from APIController import APIController

client = APIController('nba', '2017-playoff')

print('Initiated Controller')

scheduleJSON = client.getFullSchedule()

print('Completed GET')

with open('schedule_2017_playoff.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    file.writerow(['ID', 'Date', 'AwayTeamID', 'AwayTeamCity', 'AwayTeamName', 'AwayTeamAbbrev', 'HomeTeamID', 'HomeTeamCity', 'HomeTeamName', 'HomeTeamAbbrev'])

    for game in scheduleJSON['fullgameschedule']['gameentry']:
        file.writerow([game['id'],
                        game['date'],
                        game['awayTeam']['ID'],
                        game['awayTeam']['City'],
                        game['awayTeam']['Name'],
                        game['awayTeam']['Abbreviation'],
                        game['homeTeam']['ID'],
                        game['homeTeam']['City'],
                        game['homeTeam']['Name'],
                        game['homeTeam']['Abbreviation']
                       ])

print('Write Complete')
