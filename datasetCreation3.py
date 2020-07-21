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
            trainX.append(game[2:10] + game[11:])
            trainNum -=1
    with open('trainData.csv','w') as newfile:
        csv_writer = csv.writer(newfile, lineterminator = '\n')
        for data in trainX:
            csv_writer.writerow(data)
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
    
    
    
    with open('teamSeasonData.csv','r') as teamdata:
        csv_reader = csv.reader(teamdata)
        
        teamDataList =[]
        for line in csv_reader:
            teamDataList.append(line)
        
        #print(teamDataList)
        
        homeTeamData =[]
        awayTeamData =[]
        temp =[]
        for game in preset:
            for season in teamDataList:
                #   if teamID is same       if season is same
                if season[0] == game[1] and season[2][:4] == game[0][1:]:
                    avgHTFGM = float(season[8])/float(season[3])
                    temp.append(str(avgHTFGM))
                    avgHTFGA = float(season[9])/float(season[3])
                    temp.append(str(avgHTFGA))
                    avgHT3FGM = float(season[11])/float(season[3])
                    temp.append(str(avgHT3FGM))
                    avgHT3FGA = float(season[12])/float(season[3])
                    temp.append(str(avgHT3FGA))
                    avgHTPTS = float(season[27])/float(season[3])
                    temp.append(str(avgHTPTS))
                    avgHTREB = float(season[19])/float(season[3])
                    temp.append(str(avgHTREB))
                    avgHTAST = float(season[20])/float(season[3])
                    temp.append(str(avgHTAST))
                    avgHTTOV = float(season[21])/float(season[3])
                    temp.append(str(avgHTTOV))
                    homeTeamData.append(temp)
                    temp =[]
                    
                #   if teamID is same       if season is same
                if season[0] == game[10] and season[2][:4] == game[0][1:]:
                    avgATFGM = float(season[8])/float(season[3])
                    temp.append(str(avgATFGM))
                    avgATFGA = float(season[9])/float(season[3])
                    temp.append(str(avgATFGA))
                    avgAT3FGM = float(season[11])/float(season[3])
                    temp.append(str(avgAT3FGM))
                    avgAT3FGA = float(season[12])/float(season[3])
                    temp.append(str(avgAT3FGA))
                    avgATPTS = float(season[27])/float(season[3])
                    temp.append(str(avgATPTS))
                    avgATREB = float(season[19])/float(season[3])
                    temp.append(str(avgATREB))
                    avgATAST = float(season[20])/float(season[3])
                    temp.append(str(avgATAST))
                    avgATTOV = float(season[21])/float(season[3])
                    temp.append(str(avgATTOV))
                    awayTeamData.append(temp)
                    temp =[]
        
        
    with open('playerSeasonData.csv.','r') as playerdata:
            
        csv_reader = csv.reader(playerdata)
        playerData =[]
        for line in csv_reader:
            playerData.append(line)
            
        
        homePlayerData =[]
        awayPlayerData =[]
        hcount =0
        acount =0
        htemp =[]
        atemp =[]
        for game in preset:
            for player in playerData:
                # if playerID is same        if season is same
                if game[19] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)  
                    hcount+=1
                if game[27] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)
                    hcount+=1
                if game[35] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)
                    hcount+=1
                if game[43] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)
                    hcount+=1
                if game[51] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:    
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)
                    hcount+=1
                if game[59] == player[0] and game[0][1:] == player[2][:4] and game[1] == player[3]:
                    htemp.append(player[0])
                    
                    avgHPTS = float(player[30])/float(player[6])
                    htemp.append(avgHPTS)
                    
                    avgHREB = float(player[22])/float(player[6])
                    htemp.append(avgHREB)
                    
                    avgHAST = float(player[23])/float(player[6])
                    htemp.append(avgHAST)
                    
                    avgHFGA = float(player[12])/float(player[6])
                    htemp.append(avgHFGA)
                    
                    avgHFGM = float(player[11])/float(player[6])
                    htemp.append(avgHFGM)
                    
                    avgHTOV = float(player[24])/float(player[6])
                    htemp.append(avgHTOV)
                    
                    avgHPM = float(player[31])/float(player[6])
                    htemp.append(avgHPM)
                    hcount+=1
                # end of home players
                
                #if all home players are found
                if hcount ==6:
                    homePlayerData.append(htemp)
                    htemp = []
                    hcount = 0
            
                #start of away players
                if game[67] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:    
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                    
                if game[75] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:    
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                if game[83] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:  
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                if game[91] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:    
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                if game[99] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                if game[107] == player[0] and game[0][1:] == player[2][:4] and game[10] == player[3]:
                    atemp.append(player[0])
                    
                    avgAPTS = float(player[30])/float(player[6])
                    atemp.append(avgAPTS)
                    
                    avgAREB = float(player[22])/float(player[6])
                    atemp.append(avgAREB)
                    
                    avgAAST = float(player[23])/float(player[6])
                    atemp.append(avgAAST)
                    
                    avgAFGA = float(player[12])/float(player[6])
                    atemp.append(avgAFGA)
                    
                    avgAFGM = float(player[11])/float(player[6])
                    atemp.append(avgAFGM)
                    
                    avgATOV = float(player[24])/float(player[6])
                    atemp.append(avgATOV)
                    
                    avgAPM = float(player[31])/float(player[6])
                    atemp.append(avgAPM)
                    acount+=1
                if acount == 6:
                    awayPlayerData.append(atemp)
                    atemp =[]
                    acount =0
                    

        finalTestData =[]
        for j in range(len(awayTeamData)):
            new = homeTeamData[j]+awayTeamData[j] + homePlayerData[j]+ awayPlayerData[j]
            finalTestData.append(new)
    """
    with open('testData.csv','w') as new_file:
        csv_writer = csv.writer(new_file, lineterminator ='\n')
        for data in finalTestData:
            csv_writer.writerow(data)
       """     

        
getMatrices()
