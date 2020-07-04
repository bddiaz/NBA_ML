# -*- coding: utf-8 -*-
"""
Bryan Diaz


This file is for producing the appropiate dataset for my
NBA prediction Machine Learning project.

This file contains the first step of creating the dataset: 
It gathers all of the LA Lakers games from the 2012-13 season to 2019-20 season,
as well as get the statistics of every player for every one of those games. Then, 
I create a new file to store all of this data. 

I used an existing dataset from Kaggle to get all data from all teams from starting
in the 70s, and so I used the NBA API module to get game IDs from the seasons 
and teams of interest, and this data to filter out the appropiate data from the original
dataset from Kaggle.

"""

import csv

seasonDataList = []

def main():
    
    # calling getGamesData to get all the LAL game ids, date, matchup,
    # and results from the seasons given
    getGamesData('2012')
    getGamesData('2013')
    getGamesData('2014')
    getGamesData('2015')
    getGamesData('2016')
    getGamesData('2017')
    getGamesData('2018')
    getGamesData('2019')
    filterData()


# filter data 
def filterData():
    
    with open('games_details.csv', 'r') as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        
        with open('selected_game_details.csv', 'w') as new_file:
            fieldNames = ['date','matchup','WL', 'PLAYER_NAME','MIN','FGM', 'OREB', 'BLK', 'REB', 'START_POSITION', 'TEAM_CITY', 'FG3A', 'FTM', 'FT_PCT', 'DREB', 'FG3_PCT', 'FG3M', 'STL', 'GAME_ID', 'TO', 'PF', 'PLUS_MINUS', 'PTS', 'FG_PCT', 'AST', 'PLAYER_ID', 'TEAM_ID', 'COMMENT', 'FTA', 'TEAM_ABBREVIATION', 'FGA']
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldNames, lineterminator = '\n')
            csv_writer.writeheader()
            counter =0
            c = 0
            for line in csv_reader:
                c +=1
                for game in seasonDataList:
                    #match id of lakers game to ids of all game in csv file
                    if game[0] == line['GAME_ID']:
                        line['date'] = game[1]
                        line['matchup'] = game[2]
                        line['WL'] = game[3]
                        if line['COMMENT'] == '':
                            csv_writer.writerow(line)
                    else:
                        counter+=1
                print(counter)
                        
            
        
# this function uses the nba api to get the info for the LA games that we want:
# gameID, matchup, won/loss, date
def getGamesData(season):
    from nba_api.stats.endpoints import leaguegamelog  
    gamelog = leaguegamelog.LeagueGameLog(season= season)
    #get dictionary of game log for season interested in
    dictgamelog = gamelog.league_game_log.get_dict()
    counter = 0
    
    seasonData = dictgamelog['data']
    # gets all the LAL games 
    for game in seasonData:
        if game[2] == 'LAL':
            counter += 1
            # adds the fetures mentioned above
            tempList = [game[4][2:], game[5], game[6], game[7]]
            seasonDataList.append(tempList)       
    
main()
    

    





















       