# NBA_ML

Machine learning project - I am working on multiple machine learning algorithms using NBA data.

Here I both used an api to receive game data alongside an already made dataset from Kaggle to create my own dataset with the relevant data. After filtering this data
I will implement at least 2 algorithms, the first of a smaller scale and the second much larger: logistic regression and a neural network.


DEEP NEURAL NETWORK:
I have implemented a deep, 4-layer neural network which returns the probability of a home team winning a particular game against another team. 

Train data: 
I trained on 6000 NBA games, starting at the beginning of the 2012-2013 season and up until sometime in the middle of the 2016 season. One traning example had 100 features. These features included all the game data that I thought would be relevant. The features I chose for one training example included the performances (points, reb, ast, tov, plusminus) of the top six players of both teams. In addition, one training example also included the team season average for the respective seasons (such as average points, average rebounds, average assists, average tov) for both teams. I normalized this data to speed up traning and to calculate the cost more easily after each epoch of traning. After 10,000 epochs, my cost had convereged and I tested on my test data.

Test data:
My test data included all remaining NBA games starting where the last train example left off (in the 2016 season) up until the 2019 season (until the last game before the NBA bubble). This resulted in a total of 3509 games.
Instead of testing on the performances of those players (since in real life we dont know how a player will actually perform), I instead changed my test data so that instead of using the statistics for a game already played, I used the season average for the top six players for both teams (i.e. avg pts, avg ast, avg reb, avg tov, avg plusminus). This is more useful and intesting because in real life, we dont know how a player will perform, so often we base our predictions on how the player has generally been performing during the season. Since the team based features were already averages for the season, those features were kept the same. Again, I also normalized this data. 

NN results/Obseravations:
Out of the 3509 games tested, I consistenly kept predicting about 68% of the games winnner correctly. This performed much better than the logistic regression algorithm and works for any nba team or game. I believe that the high number of features were very useful as the algorithm uses a pretty full glance of both teams to make a prediction. Additionally, there is no specific feature that immediate shows who the winner is (like the total points scored at the end of the game, or all the points scored by all players of a team, since there are 15 on each team and I only chose the top 6). 
Overall trends are not able to be explicitely captured like it was for the regression algorithm, but nonetheless, this algorithm is much more powerful and more accurate than the other. 

Based on some research, the accuracy I have achieved is considerably good, and my attempt stands out amongs the other for the features I used. Many other attemps are much more limited in features, where I tried to include as many relevant ones (based from my personal experience as a basketball fan). 

Next steps:
I would like to continue to work with this dataset I have created in order to implement a more sophisticated neural network such as a RNN. However, I do not know how big of an improvement I'd see as ~70% seems to be as good as these algorithms get for sports based on the research I did. Nonetheless, it is worth a try.

Features: 
Here are all the features used in this algorithm:

'homeTeamFGM','homeTeamFGA', 'homeTeamFG3M','homeTeamFG3A','homeTeamPTS','homeTeamREB','homeTeamAST','homeTeamTOV',
'awayTeamFGM','awayTeamFGA', 'awayTeamFG3M','awayTeamFG3A','awayTeamPTS','awayTeamREB','awayTeamAST','awayTeamTOV',
'p1_pts','p1_reb','p1_ast','p1_fga','p1_fgm','p1_to','p1_plusminus',
'p2_pts','p2_reb','p2_ast','p2_fga','p2_fgm','p2_to','p2_plusminus',
'p3_pts','p3_reb','p3_ast','p3_fga','p3_fgm','p3_to','p3_plusminus',
'p4_pts','p4_reb','p4_ast','p4_fga','p4_fgm','p4_to','p4_plusminus',
'p5_pts','p5_reb','p5_ast','p5_fga','p5_fgm','p5_to','p5_plusminus',
'p6_pts','p6_reb','p6_ast','p6_fga','p6_fgm','p6_to','p6_plusminus',
'op1_pts','op1_reb','op1_ast','op1_fga','op1_fgm','op1_to','op1_plusminus',
'op2_pts','op2_reb','op2_ast','op2_fga','op2_fgm','op2_to','op2_plusminus',
'op3_pts','op3_reb','op3_ast','op3_fga','op3_fgm','op3_to','op3_plusminus',
'op4_pts','op4_reb','op4_ast','op4_fga','op4_fgm','op4_to','op4_plusminus',
'op5_pts','op5_reb','op5_ast','op5_fga','op5_fgm','op5_to','op5_plusminus',
'op6_pts','op6_reb','op6_ast','op6_fga','op6_fgm','op6_to','op6_plusminus'









LOGISTIC REGRESSION
I have implemented logistic regression and have used NBA data for the LAL lakers from seasons 2012/13 - 2019/20. I trained the on the data for the first 5 seasons out of the 
632 laker games, and tested on the remaining games. 

Features (1 training example has the follwing statistics): 
                'p1_pts','p1_reb','p1_ast',
                'p2_pts','p2_reb','p2_ast',
                'p3_pts','p3_reb','p3_ast',
                'p4_pts','p4_reb','p4_ast',
                'p5_pts','p5_reb','p5_ast',
                'p6_pts','p6_reb','p6_ast',
                'op1_pts','op1_reb','op1_ast',
                'op2_pts','op2_reb','op2_ast',
                'op3_pts','op3_reb','op3_ast',
                'op4_pts','op4_reb','op4_ast',
                'op5_pts','op5_reb','op5_ast',
                'op6_pts','op6_reb','op6_ast'
 
For the training data/ test data, there were two options that I tested. I implemented a rolling averages function which takes a training example and changes it so that it is 
the average amount of that player's pts/ast/rbs up until that game. So if game 1, the first player of the home team scored 10pts/4ast/2reb and the second game the player scored 
20pts/2ast/2reb, then the stats for the second game become 15pts/3ast/2reb since those are the averages of the scores up till then. My motivation for this was firstly because 
I wanted to give the algorithm test data that might resemble a situation in real life. If I want to use a ML algorithm, I need to predict the score 'before' the game happens, 
so I need a way to give it data for a game that hasnt happened to create a prediction. I could also train the algorithm with training data of rolling averages, which yielded 
some interesting points.

Observations:

Overall, the algorithm predicted mostly low hypothesis values when trained on non-rolling averages features and tested on rolling averages feature. There were hardly any 
predictions above .4 which meant that when tested, the probability of winning (y =1) was less than 50% every time. With boundary of .5, this yielded a prediciton percentage 
of about 47% after training on 10,000 iterations. However, because the predicitons were so low, the algorithm was simply guessing for them to lose all the time. 
This makes sense considering that during the trained years, the lakers only won more than 50% of their games in the very first season. To deal with that, I lowered the boundary 
for winning to .33. This gave me a accuracy of 57%. 

When observing the guesses, it is clear though that the lakers have generally been slowly improving over the years, especially when trained for the rolling averages data. 
When tested on non-rolling averages and trained in non-rolling averages, the algorithm clearly has an easier time as the features can really give away who wins just based off 
points. 





