# -*- coding: utf-8 -*-
"""
This file will create a numpy implementation of a deep neural network.

"""

import numpy
import csv

def getMatrices():
    Total=[]
    features =['season_id','homeTeamID','homeTeamFGM','homeTeamFGA',
               'homeTeamFG3M','homeTeamFG3A','homeTeamPTS','homeTeamREB','homeTeamAST','homeTeamTOV',
               'awayTeamID','awayTeamFGM','awayTeamFGA',
               'awayTeamFG3M','awayTeamFG3A','awayTeamPTS','awayTeamREB','awayTeamAST','awayTeamTOV',
               'p1_ID','p1_pts','p1_reb','p1_ast','p1_fga','p1_fgm','p1_to','p1_plusminus',
               'p2_ID','p2_pts','p2_reb','p2_ast','p2_fga','p2_fgm','p2_to','p2_plusminus',
               'p3_ID','p3_pts','p3_reb','p3_ast','p3_fga','p3_fgm','p3_to','p3_plusminus',
               'p4_ID','p4_pts','p4_reb','p4_ast','p4_fga','p4_fgm','p4_to','p4_plusminus',
               'p5_ID','p5_pts','p5_reb','p5_ast','p5_fga','p5_fgm','p5_to','p5_plusminus',
               'p6_ID','p6_pts','p6_reb','p6_ast','p6_fga','p6_fgm','p6_to','p6_plusminus',
               'op1_ID','op1_pts','op1_reb','op1_ast','op1_fga','op1_fgm','op1_to','op1_plusminus',
               'op2_ID','op2_pts','op2_reb','op2_ast','op2_fga','op2_fgm','op2_to','op2_plusminus',
               'op3_ID','op3_pts','op3_reb','op3_ast','op3_fga','op3_fgm','op3_to','op3_plusminus',
               'op4_ID','op4_pts','op4_reb','op4_ast','op4_fga','op4_fgm','op4_to','op4_plusminus',
               'op5_ID','op5_pts','op5_reb','op5_ast','op5_fga','op5_fgm','op5_to','op5_plusminus',
               'op6_ID','op6_pts','op6_reb','op6_ast','op6_fga','op6_fgm','op6_to','op6_plusminus']
 
    
    """Get features for train/test data"""
    
    with open('Datasets/allFeaturesData.csv', 'r') as featuresFile:
        csv_reader= csv.DictReader(featuresFile)
        temp =[]
        for line in csv_reader:
            for feature in features:
                temp.append(line[feature])
            Total.append(temp)
            temp =[]
            
            
            
    """Get player IDs"""
    playerIDs =[]
    indices = [19,27,35,43,51,59,67,75,83,91,99,107]
    for game in Total:
        for index in indices:    
            if (game[index] in playerIDs)== False:
                playerIDs.append(game[index])

    
    
    
    """ Use NBA api to find season statistics for all the players in the data.
    """
    """
    allPlayersSeasonInfo =[]
    from nba_api.stats.endpoints import playerdashboardbyyearoveryear as pd
    
    for pID in playerIDs:
        
        playerDashboard = pd.PlayerDashboardByYearOverYear(player_id = pID)
        dictdashboard = playerDashboard.by_year_player_dashboard.get_dict()
        playerSeasonInfo = dictdashboard['data']
        for season in playerSeasonInfo:
            season.insert(0,pID)
        allPlayersSeasonInfo.append(playerSeasonInfo)
    """
    
    """ Create a new csv file with every players season performance 
        per line. This will be used to create the test set
    """    
    """
    with open('playerSeasonData.csv','w') as newFile:
        csv_writer = csv.writer(newFile, lineterminator ='\n')
        
        for player in allPlayersSeasonInfo:
            for year in player:
                csv_writer.writerow(year)
                """
    
     
    """ Get team IDs"""
    """
    teamIDs =[]
    tIndices =[1,10]
    for game in Total:
        for index in tIndices:
            if (game[index] in teamIDs) == False:
                teamIDs.append(game[index])
                
    """
            
    """ Use NBA apit to find team statistics of every season"""
    """
    allTeamsSeasonInfo =[]
    from nba_api.stats.endpoints import teamdashboardbyyearoveryear as td
    
    for tID in teamIDs:
        teamDashboard = td.TeamDashboardByYearOverYear(team_id = tID)
        dictTDashboard = teamDashboard.by_year_team_dashboard.get_dict()
        teamSeasonInfo = dictTDashboard['data']
        for season in teamSeasonInfo:
            season.insert(0,tID)
        allTeamsSeasonInfo.append(teamSeasonInfo)
        
    """
    
    """ create new csv file to store the season stats of every team """
    """
    with open('teamSeasonData.csv','w') as newFile:
        csv_writer = csv.writer(newFile, lineterminator='\n')
        
        for team in allTeamsSeasonInfo:
            for year in team:
                csv_writer.writerow(year)
    """
    

    trainX =[]
    #testX =[]
    trainY = []
    #testY =[]
    trainNum = 6000
    #testNum = 3509
    
    for game in Total[::-1]:
        if trainNum >0:
            trainX.append(game)
            trainNum -=1
            
    trainNum = 6000
    
    for game in Total[::-1]:
        if trainNum>0:
            if game[5] > game[13]:
                trainY.append(1)
            else:
                trainY.append(0)
            trainNum-= 1
            
            
            
    preset =[]      
    for i in range(0,3509)[::-1]:
        preset.append(Total[i])
    
    
    testFeatures = ['homeTeamFGM','homeTeamFGA',
               'homeTeamFG3M','homeTeamFG3A','homeTeamPTS','homeTeamREB','homeTeamAST','homeTeamTOV',
               'awayTeamFGM','awayTeamFGA',
               'awayTeamFG3M','awayTeamFG3A','awayTeamPTS','awayTeamREB','awayTeamAST','awayTeamTOV',
               'p1_ID','p1_pts','p1_reb','p1_ast','p1_fga','p1_fgm','p1_to','p1_plusminus',
               'p2_ID','p2_pts','p2_reb','p2_ast','p2_fga','p2_fgm','p2_to','p2_plusminus',
               'p3_ID','p3_pts','p3_reb','p3_ast','p3_fga','p3_fgm','p3_to','p3_plusminus',
               'p4_ID','p4_pts','p4_reb','p4_ast','p4_fga','p4_fgm','p4_to','p4_plusminus',
               'p5_ID','p5_pts','p5_reb','p5_ast','p5_fga','p5_fgm','p5_to','p5_plusminus',
               'p6_ID','p6_pts','p6_reb','p6_ast','p6_fga','p6_fgm','p6_to','p6_plusminus',
               'op1_ID','op1_pts','op1_reb','op1_ast','op1_fga','op1_fgm','op1_to','op1_plusminus',
               'op2_ID','op2_pts','op2_reb','op2_ast','op2_fga','op2_fgm','op2_to','op2_plusminus',
               'op3_ID','op3_pts','op3_reb','op3_ast','op3_fga','op3_fgm','op3_to','op3_plusminus',
               'op4_ID','op4_pts','op4_reb','op4_ast','op4_fga','op4_fgm','op4_to','op4_plusminus',
               'op5_ID','op5_pts','op5_reb','op5_ast','op5_fga','op5_fgm','op5_to','op5_plusminus',
               'op6_ID','op6_pts','op6_reb','op6_ast','op6_fga','op6_fgm','op6_to','op6_plusminus']
    
    
    with open('teamSeasonData.csv','r') as teamdata:
        csv_reader = csv.reader(teamdata)
    
        for line in csv_reader:
            for game in preset:
                temp = []
                if game[0][1:] == line[3][:4]:
                    if game[1] == line[0]:
                        avgHTFGM = float(line[7]/line[2])
                        temp.append(str(avgHTFGM))
                        avgHTFGA = float(line[8]/line[2])
                        temp.append(str(avgHTFGA))
                        avgHT3FGM = float(line[10]/line[2])
                        temp.append(str(avgHT3FGM))
                        avgHT3FGA = float(line[11]/line[2])
                        temp.append(str(avgHT3FGA))
                        avgHTPTS = float(line[26]/line[2])
                        temp.append(str(avgHTPTS))
                        avgHTREB = float(line[18]/line[2])
                        temp.append(str(avgHTREB))
                        avgHTAST = float(line[19]/line[2])
                        temp.append(str(avgHTAST))
                        avgHTTOV = float(line[20]/line[2])
                        temp.append(str(avgHTTOV))
                    if game[10] == line[0]:
                        avgATFGM = float(line[7]/line[2])
                        temp.append(str(avgATFGM))
                        avgATFGA = float(line[8]/line[2])
                        temp.append(str(avgATFGA))
                        avgAT3FGM = float(line[10]/line[2])
                        temp.append(str(avgAT3FGM))
                        avgAT3FGA = float(line[11]/line[2])
                        temp.append(str(avgAT3FGA))
                        avgATPTS = float(line[26]/line[2])
                        temp.append(str(avgATPTS))
                        avgATREB = float(line[18]/line[2])
                        temp.append(str(avgATREB))
                        avgATAST = float(line[19]/line[2])
                        temp.append(str(avgATAST))
                        avgATTOV = float(line[20]/line[2])
                        temp.append(str(avgATTOV))
getMatrices()
