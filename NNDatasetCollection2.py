# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:22:56 2020

@author: 17732
"""

import csv

gameList = []
homePlayerList = []
awayPlayerList = []  

def getPlayerDetails():
    
    featureList= ['PLAYER_NAME','PLAYER_ID','PTS','REB','AST','FGA','FGM','TO','PLUS_MINUS']
    
    with open('allPlayerDetailHome.csv', 'r') as hPlayerFile:
        csv_reader = csv.DictReader(hPlayerFile)
        current = '21900895'
        gameList.append(current)
        temp =[]
        nHPlayers =0
        for line in csv_reader:
            if current == line['GAME_ID']:
                if nHPlayers <6:
                    for feature in featureList:
                        temp.append(line[feature])
                    nHPlayers+=1
                if nHPlayers ==6 and current == '21200001':
                    homePlayerList.append(temp)
                    nHPlayers =7
            else:
                homePlayerList.append(temp)
                temp =[]
                current = line['GAME_ID']
                gameList.append(current)
                for feature in featureList:
                    temp.append(line[feature])
                nHPlayers = 1
                
    #print(gameList)    
    with open('allPlayerDetailAway.csv','r') as aPlayerFile:
        csv_reader = csv.DictReader(aPlayerFile)
        current = '21900895'
        nAPlayers =0
        temp =[]
        for line in csv_reader:
            if current == line['GAME_ID']:
                if nAPlayers <6:
                    for feature in featureList:
                        temp.append(line[feature])
                    nAPlayers+=1
                if nAPlayers ==6 and current == '21200001':
                    awayPlayerList.append(temp)
                    nAPlayers =7
            else:
                awayPlayerList.append(temp)
                temp = []
                current =line['GAME_ID']
                for feature in featureList:
                    temp.append(line[feature])
                nAPlayers =1
                
        
          
awayTeamList=[]
homeTeamList=[]
def getTeamDetails():
    teamFeatures = ['TEAM_ABBREVIATION','TEAM_ID','FGM','FGA','FG3M','FG3A','PTS','REB','AST','TOV']
    with open('allGamesTeamData.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count =0
        hcount =0
        for line in csv_reader:
            for game in gameList:
                if line['GAME_ID'][2:] == game and line['MATCHUP'][4]  == '@':
                    count+=1
                    temp =[]
                    for feature in teamFeatures:
                        temp.append(line[feature])
                    awayTeamList.append(temp)
                    
                    
                if line['GAME_ID'][2:]== game and line['MATCHUP'][4]  != '@':
                    hcount+=1
                    temp =[]
                    temp.append(line['GAME_ID'][2:])
                    temp.append(line['SEASON_ID'])
                    for feature in teamFeatures:
                        temp.append(line[feature])
                    homeTeamList.append(temp)


def organizeDataAndMakeCSV():
    allGameData =[]
    temp =[]
    for i in range(len(gameList)):
        for j in range(len(homeTeamList)):
            if homeTeamList[j][0] == gameList[i]:
                #print('hiss')
                #temp.append(gameList[i])
                temp+= homeTeamList[j] + awayTeamList[j]+ homePlayerList[i]+ awayPlayerList[i]
                allGameData.append(temp)
                temp =[]

    
    with open('allFeaturesData.csv', 'w') as new_file:
        fieldNames = ['gameID','season_id','homeTeam','homeTeamID','homeTeamFGM','homeTeamFGA',
                      'homeTeamFG3M','homeTeamFG3A','homeTeamPTS','homeTeamREB','homeTeamAST','homeTeamTOV',
                      'awayTeam','awayTeamID','awayTeamFGM','awayTeamFGA',
                      'awayTeamFG3M','awayTeamFG3A','awayTeamPTS','awayTeamREB','awayTeamAST','awayTeamTOV',
                          'p1_name','p1_ID','p1_pts','p1_reb','p1_ast','p1_fga','p1_fgm','p1_to','p1_plusminus',
                          'p2_name','p2_ID','p2_pts','p2_reb','p2_ast','p2_fga','p2_fgm','p2_to','p2_plusminus',
                          'p3_name','p3_ID','p3_pts','p3_reb','p3_ast','p3_fga','p3_fgm','p3_to','p3_plusminus',
                          'p4_name','p4_ID','p4_pts','p4_reb','p4_ast','p4_fga','p4_fgm','p4_to','p4_plusminus',
                          'p5_name','p5_ID','p5_pts','p5_reb','p5_ast','p5_fga','p5_fgm','p5_to','p5_plusminus',
                          'p6_name','p6_ID','p6_pts','p6_reb','p6_ast','p6_fga','p6_fgm','p6_to','p6_plusminus',
                          'op1_name','op1_ID','op1_pts','op1_reb','op1_ast','op1_fga','op1_fgm','op1_to','op1_plusminus',
                          'op2_name','op2_ID','op2_pts','op2_reb','op2_ast','op2_fga','op2_fgm','op2_to','op2_plusminus',
                          'op3_name','op3_ID','op3_pts','op3_reb','op3_ast','op3_fga','op3_fgm','op3_to','op3_plusminus',
                          'op4_name','op4_ID','op4_pts','op4_reb','op4_ast','op4_fga','op4_fgm','op4_to','op4_plusminus',
                          'op5_name','op5_ID','op5_pts','op5_reb','op5_ast','op5_fga','op5_fgm','op5_to','op5_plusminus',
                          'op6_name','op6_ID','op6_pts','op6_reb','op6_ast','op6_fga','op6_fgm','op6_to','op6_plusminus',]
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldNames, lineterminator ='\n')
        csv_writer.writeheader()
        
        entry = {}
        for game in allGameData:
            for i in range(len(game)):
                entry[fieldNames[i]] = game[i]
            csv_writer.writerow(entry)
            entry ={}
                
                    
        
        
    
        
        

getPlayerDetails()  
getTeamDetails()
organizeDataAndMakeCSV()


    
                    
        