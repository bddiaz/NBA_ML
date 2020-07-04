# -*- coding: utf-8 -*-
"""
Part 2 of the dataset creation

Here, I will use the newly made csv file with all the relevant game and player data
and will format it so it is ready for the logistic regression algorithm.

Concretly, every line will be 1 game. This line will include the top 6 players from both
teams, and all of their stats.

Bryan Diaz
"""

import csv
listOfGames = []

# this function takes all statistics of the top 6 players of all the LAL
# games and the top 6 players of the opposite team and adds them to 1 list. 
# once this list has all the statistics of this game, the list is added to 
# listOfGames, and then a new list is created for the next game.
def groupGameData():
    # starting game ID
    current = '21900900'
    
    with open('selected_game_details.csv', 'r') as csv_file:
        #num of home players 
        numPlayers =0
        #num of opposition players
        numOPlayers =0
        csv_reader = csv.DictReader(csv_file)
        #temp list holds all the scores of the top 6 players and other data
        temp=[]
        #first variable for time filling in the temp list with other data first
        first = True
        # constant variable to see the order to fill in data in temp list. (append vs. insert())
        c = 'LAL'
        # if the first player from the new game id is not an LAL player, then 
        # we append the oppositional players first, then insert at the begging the LA players
        # to keep same order
        reverse = False
        #features to add in game data list per player
        features =['PLAYER_NAME','FGM','MIN','TO', 'AST', 'FG3M','FGM', 'FTM', 'PTS','REB','FG_PCT','PLUS_MINUS']
        for line in csv_reader:
            # if we are still filling in the data for the same game id
            if line['GAME_ID'] == current:
                # fill in the first 6 LAL players. 
                if numPlayers <6 and line['TEAM_ABBREVIATION'] == c:
                    # 'reverse' inserting because oppositional team went first
                    if reverse == True:
                        for i in range(len(features)):
                            temp.insert(4+i+(12*numPlayers),line[features[i]])
                        numPlayers+=1
                    else:
                        # if adding LAL players first 
                        if first == True:
                            temp.append(line['date'])
                            temp.append(line['matchup'])
                            temp.append(current)
                            temp.append(line['WL'])
                            first = False
                        for feature in features:
                            temp.append(line[feature])
                        numPlayers+=1
                #if adding oppositional characters first
                if numOPlayers < 6 and line['TEAM_ABBREVIATION'] != c: 
                    for feature in features:
                        temp.append(line[feature])
                    numOPlayers+=1
            # else statement for when the game id is different from before, and so
            # we have to add the temp list to the listOfGames variable, and start again 
            # with a new empty temp list, and add players. This is where we check if we go 
            # in reverse order
            else:
                current = line['GAME_ID']
                listOfGames.append(temp)
                temp =[]
                #checks if we are going in right order
                if line['TEAM_ABBREVIATION'] == c:
                    # reverse = false means we are in right order (LAL --> OPTEAM)
                    reverse = False
                    numOPlayers =0
                    # add the first player of LAL team
                    temp.append(line['date'])
                    temp.append(line['matchup'])
                    temp.append(current)
                    temp.append(line['WL'])
                    for feature in features:
                        temp.append(line[feature])
                    numPlayers =1
                # if other team is first
                else:
                    # since its the other team first, we add the first oppositional 
                    # player and set reverse to true for when we add the LAL players
                    temp.append(line['date'])
                    temp.append(line['matchup'])
                    temp.append(current)
                    temp.append(line['WL'])
                    numPlayers = 0
                    reverse = True
                    for feature in features:
                        temp.append(line[feature])
                    numOPlayers =1
                    
                

# this function converts the lists inside listOfGames into dictionary
# entrys. This allows us to create 
def list2Dictionary():
    entry = {}
    with open('semifinaldataset.csv','w') as new_file:
        # fieldnames constains all the categories we're interested in
            fieldNames = ['date','matchup','game_id','result',
                          'p1_name','p1_pts','p1_reb','p1_ast',
                          'p2_name','p2_pts','p2_reb','p2_ast',
                          'p3_name','p3_pts','p3_reb','p3_ast',
                          'p4_name','p4_pts','p4_reb','p4_ast',
                          'p5_name','p5_pts','p5_reb','p5_ast',
                          'p6_name','p6_pts','p6_reb','p6_ast',
                          'op1_name','op1_pts','op1_reb','op1_ast',
                          'op2_name','op2_pts','op2_reb','op2_ast',
                          'op3_name','op3_pts','op3_reb','op3_ast',
                          'op4_name','op4_pts','op4_reb','op4_ast',
                          'op5_name','op5_pts','op5_reb','op5_ast',
                          'op6_name','op6_pts','op6_reb','op6_ast']
            csv_writer = csv.DictWriter(new_file, fieldnames= fieldNames, lineterminator = '\n')
            csv_writer.writeheader()
            # these for loops create 
            for game in listOfGames:
                entry['date']= game[0]
                entry['matchup']= game[1]
                entry['game_id']=game[2]
                entry['result']=game[3]
                for i in range(6):
                    e = 'p'+str(i+1)+'_name'
                    entry[e] = game[4+12*i]
                    e = 'p'+str(i+1)+'_pts'
                    entry[e] = game[12+12*i]
                    e = 'p'+str(i+1)+'_reb'
                    entry[e] = game[13+12*i]
                    e = 'p'+str(i+1)+'_ast'
                    entry[e] = game[8+12*i]
                
                for i in range(6):
                    e = 'op'+str(i+1)+'_name'
                    entry[e] = game[76+12*i]
                    e = 'op'+str(i+1)+'_pts'
                    entry[e] = game[84+12*i]
                    e = 'op'+str(i+1)+'_reb'
                    entry[e] = game[85+12*i]
                    e = 'op'+str(i+1)+'_ast'
                    entry[e] = game[80+12*i]
        
                csv_writer.writerow(entry)
                entry ={}
        
    
        
        
        
        
        

groupGameData()
list2Dictionary()


    
    
    
    
    
    
         

