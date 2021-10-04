# Practica 5
### Por:
### Alvaro Bryan Cori Sanchez
### Omar Arias

## Description Of Problem
The tic tac toe is a simple game which is based on aligning n marcs (X or O) in order vertical, horizontal and diagonal completing all the squares with a unique marc (or only X or only O) above a table with the purpose of win the game if you complete a line. The game is for two persons or well one person and a machine.
When a tic tac toe game begins first one person put in the table a mark (X or O) then the rival put the adversarial mark in a position of the table, well how we can program this for two persons or even better as implementing an intelligent machine that challenges a person.

## Description Of the Solution
The problem know as adversarial algorithm needs two types of game. A player vs player and a player vs machine. Implement a game with two players are known but long to implement. But with the machine we need to implement a algorithm that see the next steps of the adversarial and take the best request to the machine can take the decision of mark a square and challenge a person.
We use:
Min Max.- The algorithm explores a tree with all the states possible and take the max or the min value of victory in order to take the best benefit for the machine.
Min Max Pruning. - The algorithm implements the same logic of Min Max, this algorithm also cut the branch that we know that we don’t need because we get a response in a branch that be the max or the min solution by the father of the branches.
First, we get a table 3x3, 4x4 or 5x5 then the first player marks a position and be the turn of the second player. We repeat these cases until we get a table without free spaces.
The things we need to implement are:
Initial State: A table without any mark or with squares non used.
Final State: In the table are no more possible moves, a table without squares not used or a state that one contender can get a victory.
 Players: Player_min(X), Player_max(O)
Actions: Put a mark in a free space of the table.
Results: The result is a free space marked with one contender.
Utility: Return the number of results in the table.
Terminal test: Return the result in terms of gain or lossy. -2 already exits squares without a mark and no one have a line of victory in the table, -1 if the min win (X), 1 if max win, 0 means a draw.


We implement dictionaries because is more fast pass a dictionary than calculate in every called at the function min or max.
In the algorithm min_max
When we recalculate the possible results we get in seconds 9.52s, 8.82s, 9.05s, 14.02s and 10.46s
When we save actions in dictionaries the possible results we get in seconds 7.57s, 7.63s, 7.48s, 7.39s and 8.06s


Experiments with Min Max
--------------------------------

We play against the algorithm, and the results are the next:

| Tic Tac Toe  | Expanded states |  Total States |
| :------:  | :-----------------: | :-----------: |
|  3x3     |    1rs move, 2nd move,etc  | Total   |
|  N° 1    |    549945, 7331, 197, 13, 1   | 557487 |
|  N° 2    |       549945, 8231, 245, 11     | 558432 |
|  N° 3    |     549945, 7331, 197, 13, 1      | 557487|
|  N° 4    |     549945, 7583, 124, 8      | 557660 |
|  N° 5    |      549945, 7583, 173, 8    | 557709 |
|  Average   |      549945, 7611.8,  187.2 , 10.6, 0.4  | 557755 |


Experiments with Min Max +  AlphaBeta Prunning
-----------------------------------------------

| Tic Tac Toe  |  Expanded states | Total States | 
| :------: | :-----------------: | :-----------: |
|  3x3     |   1rs move, 2nd move,etc  |      Total  |
|  N° 1    |    66453, 1253, 42, 13, 1   |  67762 |
|  N° 2    |     66453, 1253, 42    | 67748 | 
|  N° 3    |       66453, 3792, 122, 9     | 70376 |
|  N° 4    |     66453, 4164, 142, 10     | 70769 |
|  N° 5    |     66453, 1592, 205, 11   | 68261 |
|  Average   |                         | 68983.2     |

Experiments with Min Max +  Cut Off
-----------------------------------------------

| Tic Tac Toe  |  Expanded states | Total States | 
| :------: | :---------------: | :-----------------: | :-----------: |
|  3x3     |     1rs move, 2nd move,etc  |      Total  |
|  N° 1    |     22219, 23012, 23069, 23084  |  91384 |
|  N° 2    |      45303, 46096, 46153, 46168   | 183720 | 
|  N° 3    |    68387, 78691, 79016    | 226094 |
|  N° 4    |      101235, 109071, 109356   | 319662 |
|  N° 5    |   131575, 132368, 132425, 132440  | 528808 |
|  Average   |                        | 269933.6     |




## How many states does the game tree have for a 3x3, 4x4 and 5x5 board?
The case depends in each case how we can see in the tables


| 3X3   |Min Max            |  Min Max Prunning   | Cut Off            |
| :------: | :---------------: | :-----------------: | :-----------------:|
|   9      |  549945 	       |   66453  	     |    3253 		  |  
|   7      |   7331  	       |    1253  	     |    4839  	  |   
|   5      |  197 	       |    42  	     |    4873  	  |   
|   3      |  13  	       |    13  	     |    4877  	  |  
|   1      |  1  	       |    1   	     |    4873  	  |   
|  TOTAL   | 557487  	       |   67762  	     |    22715  	  |  



| 3X3 <td  |Min Max            |  Min Max Prunning   | Cut Off            |
| :------: | :---------------: | :-----------------: | :-----------------:|
|   8      |  55504	       |   24802  	     |    3253 		  |  
|   6      |   935  	       |    377  	     |    4849  	  |   
|   4      |  50	       |    44  	     |    4899  	  |   
|   2      |  4  	       |     4  	     |    4903  	  |  
|  TOTAL   | 56493 	       |   25227  	     |    17904  	  |  


## What is the algorithm that takes more (less) and expands more (less) states? MinMax, MinMax + AlphaBeta Prunning or MinMaxCutoff?

#### 3x3
The Min max take 1.2 seg and 1.1 segs in average.

The states expanded is the worst when the pc take first turn.
The states expanded is the worst when the pc take second turn.

The Min max prunning take 0.22 segs and 0.1157 segs in average.

The states expanded is in the middle when the pc take first turn.
The states expanded is in the middle when the pc take second turn.

The cut off take 0.22 segs and 0.11 segs  0.03 segs in average.


The states expanded is in the best when the pc take first turn.
The states expanded is in the best when the pc take second turn.


Conclusions 
=====================

The best algorithm is the cut off, because we can cut to a certain level so that optimizing the time is even the one that takes less time to realize it.

The middle algorithm is the  prunning, because this cut brands and not examine all the cases.

The worst algorithm is the min max, because this take all the cases and take a large time.

All algorithms can responde in reasonable time on the 3x3 board, but when it does on the 4x4 board only the cut off can do it in optimal time and the prunning takes more than 7 minutes to respond. For the 5x5 board only the cut off can respond in time. The min max algorithm is only optimal if used on the 3x3 board.

## Bibliography
### reduce
https://www.geeksforgeeks.org/reduce-in-python/

### dictionary
https://realpython.com/iterate-through-dictionary-python/
https://stackoverflow.com/questions/9358983/dictionaries-and-default-values

### numpy array
https://numpy.org/doc/stable/reference/generated/numpy.array.html

