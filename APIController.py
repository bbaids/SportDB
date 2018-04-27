import requests
import base64
import configuration
from datetime import datetime

class APIController:

    format = 'json'
    baseURL = configuration.baseURL
    username = configuration.username
    password = configuration.password
    
    def __init__(self, sport, season, forDate = datetime.now().strftime("%Y%m%d")):
        self.sport = sport
        self.season = season
        self.forDate = forDate

    def buildURL(self):
        requestURL = self.baseURL + '/' + self.sport + '/' + self.season
        return str(requestURL)

############### GET PLAYERS #########################################
    def getPlayers(self, team = None, player = None, rosterStatus = None):
        try:
            controllerURL = self.buildURL()
            requestURL = str(controllerURL + '/' + 'roster_players.' + self.format)
            params = {
                    "fordate": self.forDate
                    , "team": team
                    , "player": player
                    , "rosterStatus": rosterStatus
                    }
            headers = {
                    "Authorization": "Basic " + base64.b64encode('{}:{}'.format(self.username,self.password).encode('utf-8')).decode('ascii')
                    }   
            
            response = requests.get(url = requestURL, params = params, headers = headers)

            if(requests.codes.ok == response.status_code):
               return response.json()

            else:
               print('getPlayers Request Failed')
               print(response.status_code)
               print(response.request.url)
               
        except exception as e:
            print('getPlayers encountered an error')
            print(str(e))

############### GET FULL SCHEDULE ###################################
    def getFullSchedule(self, team = None, date = None):
        try:
            requestForDate = self.forDate
            controllerURL = self.buildURL()
            requestURL = str(controllerURL + '/' + 'full_game_schedule.' + self.format)
            params = {
                    "team": team
                    , "date": date 
                    }
            headers = {
                    "Authorization": "Basic " + base64.b64encode('{}:{}'.format(self.username,self.password).encode('utf-8')).decode('ascii')
                    }   
            
            response = requests.get(url = requestURL, params = params, headers = headers)

            if(requests.codes.ok == response.status_code):
               return response.json()

            else:
               print('getFullSchedule Request Failed')
               print(response.status_code)
               print(response.request.url)
            
        except exception as e:
            print('getFullSchedule encountered an error')
            print(str(e))

############### GET PLAYER GAME STATISTICS ###################################
    def getPlayerGamelogs(self, team = None, player = None, game = None, date = None, playerstats = None):
        try:
            requestForDate = self.forDate
            controllerURL = self.buildURL()
            requestURL = str(controllerURL + '/' + 'player_gamelogs.' + self.format)
            params = {
                    "team": team
                    , "player": player
                    , "game": game
                    , "date": date
                    , "playerstats": playerstats
                    }
            headers = {
                    "Authorization": "Basic " + base64.b64encode('{}:{}'.format(self.username,self.password).encode('utf-8')).decode('ascii')
                    }   
            
            response = requests.get(url = requestURL, params = params, headers = headers)

            if(response.status_code == requests.codes.ok):
                return response.json()

            else:
                print('getPlayerGamelogs GET request was not successful')
                print(response.status_code)
                print(response.request.url)
            
        except requests.exceptions.RequestException as e:
            print('getPlayerGamelogs encountered an error')
            print(str(e))
