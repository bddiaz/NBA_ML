# NBA_ML

Machine learning project - I am working on multiple machine learning algorithms using NBA data.

Here I both used an api to receive game data alongside an already made dataset from Kaggle to create my own dataset with the relevant data. After filtering this data
I will implement at least 2 algorithms, the first of a smaller scale and the second much larger: logistic regression and a neural network.


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





