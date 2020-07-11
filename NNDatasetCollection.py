# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:34:16 2020

@author: 17732
"""

import csv
"""
from nba_api.stats.endpoints import leaguegamelog  
seasons = ['2012','2013','2014','2015','2016','2017','2018','2019']
gameList = []
for season in seasons:
    gamelog = leaguegamelog.LeagueGameLog(season= season)
    #get dictionary of game log for season interested in
    dictgamelog = gamelog.league_game_log.get_dict()
        
    #print(dictgamelog['headers'])
    count = 0
    acount =0
    justdata = dictgamelog['data']
    for game in justdata:
        gameList.append(game)

"""

from nba_api.stats.endpoints import leaguegamelog  
seasons = ['2012','2013','2014','2015','2016','2017','2018','2019']
gameList = []
for season in seasons:
    gamelog = leaguegamelog.LeagueGameLog(season= season)
    #get dictionary of game log for season interested in
    dictgamelog = gamelog.league_game_log.get_dict()
        
    #print(dictgamelog['headers'])
    count = 0
    acount =0
    print(dictgamelog['headers'])
    justdata = dictgamelog['data']
    for game in justdata:
        if game[6][4:7] == 'vs.':
            gameList.append(game)
"""

with open('games_details.csv','r') as details_file:
    ca =0
    csv_reader = csv.DictReader(details_file)
    with open('allPlayerDetailHome.csv', 'w') as new_file2:
        fieldNames= ['PLAYER_NAME','MIN','FGM', 'OREB', 'BLK', 'REB', 'START_POSITION', 'TEAM_CITY', 'FG3A', 'FTM', 'FT_PCT', 'DREB', 'FG3_PCT', 'FG3M', 'STL', 'GAME_ID', 'TO', 'PF', 'PLUS_MINUS', 'PTS', 'FG_PCT', 'AST', 'PLAYER_ID', 'TEAM_ID', 'COMMENT', 'FTA', 'TEAM_ABBREVIATION', 'FGA']

        csv_writer = csv.DictWriter(new_file2, fieldnames = fieldNames,lineterminator = '\n')
        csv_writer.writeheader()
        for line in csv_reader:
            
            for game in gameList:
                
                if game[4][2:] == line['GAME_ID'] and game[2] == line['TEAM_ABBREVIATION']:
                    if line['COMMENT'] == '':
                        ch +=1
                        csv_writer.writerow(line)

"""
with open('games_details.csv','r') as details_file:
    ca =0
    csv_reader = csv.DictReader(details_file)
    with open('allPlayerDetailAway.csv', 'w') as new_file3:
        fieldNames= ['PLAYER_NAME','MIN','FGM', 'OREB', 'BLK', 'REB', 'START_POSITION', 'TEAM_CITY', 'FG3A', 'FTM', 'FT_PCT', 'DREB', 'FG3_PCT', 'FG3M', 'STL', 'GAME_ID', 'TO', 'PF', 'PLUS_MINUS', 'PTS', 'FG_PCT', 'AST', 'PLAYER_ID', 'TEAM_ID', 'COMMENT', 'FTA', 'TEAM_ABBREVIATION', 'FGA']

        csv_writer = csv.DictWriter(new_file3, fieldnames = fieldNames,lineterminator = '\n')
        csv_writer.writeheader()
        for line in csv_reader:
            
            for game in gameList:
                
                if game[4][2:] == line['GAME_ID'] and game[2] != line['TEAM_ABBREVIATION']:
                    if line['COMMENT'] == '':
                        ca+=1
                        csv_writer.writerow(line)
                        
    print('home count: ' + str(ch))
    print('away count: '+ str(ca))
                    
                    
                
    
    
"""
with open('games_details.csv','r') as details_file:
    csv_reader = csv.DictReader(details_file)
    count =0
    with open ('allPlayersData.csv', 'w') as new_file1:
        fieldNames= ['PLAYER_NAME','MIN','FGM', 'OREB', 'BLK', 'REB', 'START_POSITION', 'TEAM_CITY', 'FG3A', 'FTM', 'FT_PCT', 'DREB', 'FG3_PCT', 'FG3M', 'STL', 'GAME_ID', 'TO', 'PF', 'PLUS_MINUS', 'PTS', 'FG_PCT', 'AST', 'PLAYER_ID', 'TEAM_ID', 'COMMENT', 'FTA', 'TEAM_ABBREVIATION', 'FGA']
        csv_writer = csv.DictWriter(new_file1, fieldnames = fieldNames, lineterminator = '\n')
        csv_writer.writeheader()
        for line in csv_reader:
            
            for game in gameList:
                if line['GAME_ID'] == game[4][2:]:
                    if line['COMMENT'] == '':
                        csv_writer.writerow(line)
                    
                    #print(count)

             

with open('allGamesTeamData.csv','w') as new_file:
    fieldNames = ['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 
                  'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 
                  'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 
                  'PLUS_MINUS']
    
    csv_writer = csv.writer(new_file,lineterminator = '\n')
    csv_writer.writerow(fieldNames)
    #csv_writer = csv.DictWriter(new_file, fieldnames = fieldNames)
    #csv_writer.writeheader()
    for g in gameList:
        csv_writer.writerow(g)
"""