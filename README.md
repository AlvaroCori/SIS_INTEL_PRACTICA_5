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
Min Max Prunning. - The algorithm implements the same logic of Min Max, this algorithm also cut the branch that we know that we don’t need because we get a response in a branch that be the max or the min solution by the father of the branches.
Cut Off.- The cut off algorithm is similar at the Min Max Prunning with the difference of we implement a different end case for the recursive functions, with a some depth the algorithm looks for a heuristic that allows us to obtain a value of if it is gaining maximum or minimum.

We implement two cut off heucharistics:
1 .- Heuristic of counting alienated pieces, this heuristic counts each row horizontally, vertically and diagonally if this row contains squares marked in favor and empty squares add the squares, if it has squares marked in favor and squares marked with enemy marks add 0.

2 .- Heuristic of depth.- This heuristic gets the result of the board and interprets it in different ways, if in the board are won the positive pieces rettorna 100 multiplied with the difference between the final depth plus one less the depth in which the state is found.
If he’s earning minimum returns the same but negative, if a square is greater than the first position and last position of the rows and columns returns a 20 if this in the limits returns a 10 squares are added with the same mark and subtracted with those of the rival mark depending on whether it is a maximum or minimum mark.

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

## Training heucharist 

The training heucaristic is a original algorithm, that analyzes the actual state, searching for the best row, the worse row, the best col, and the worse col, then calculate a value for utility to say if the actual state is advantageous or disadvantageous.
The logid that it uses is:
If a row/col is empty, its value is 1 point, because it could be a possible victory.
If the row/col has at least one "X", and one "O", its value is 0 point, because there can no longer be a win or a loss on this row/col.
Then depends if the analize its for "X"'s or "O"'s, supposing that its for "X"'s':
If the row/col only has "X"'s, its utility is the amount of "X"'s plus one, because only 1 is for empty rows/cols.
If the row/col only has "O";s, its utility is the amount of "O"'s, but with negative value, to point out that he is losing.

It has the same logic to diagonals, and for the analysis of the "O"'s.

We create a algorith that can return a coordenate using only this analysis, and some default posicions, to make another form to play Tic Tac Toe agains the machine, but this algorithm doesn't use recursion, so we use this algorithm like a trainer to the other algorithms.
This algorithm is original thinked to 5 in line (Tic Tac Toe 5x5), but it is worth to 3 in line too (Tic Tac Toe 3x3). But it has problems with 4 in line (Tic Tac Toe 4x4), because it hasn't a center, and maybe there are exceptions that we have to add to the algorithm so that it is also effective with 4 in line.

Like a heucharistic, it only has an analysis to the state, and return a utility, but like an algorithm to has return a coordenate, it doesn't use recursive, so it doesn't expands states, just analyze the current state with a better and worse row/col logic, and reinforces his better row/col if the worse row/col it doesn't mean that it's losing.


## How many states does the game tree have for a 3x3, 4x4 and 5x5 board?

Now we compare all the results obtained for all the algorithms Min Max, Min Max Prunning, Cut Off counting the marks and the Cut Off
using the depth and squares with more angules, we implemented in tables.

Experiments with Min Max
--------------------------------

The reason because we use dictionary is for when we recalculate the actions avaliable we got in seconds 9.52s, 8.82s, 9.05s, 14.02s and 10.46s
When we save actions in dictionaries and pass a the next called the possible results we got in seconds 7.57s, 7.63s, 7.48s, 7.39s and 8.06s

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

Experiments with Min Max +  Cut Off + Count marks aliegned
-----------------------------------------------------------

| Tic Tac Toe  |  Expanded states  |    Total States     | 
| :------:     | :---------------: | :-----------------: |
|  3x3         |     1rs move, 2nd move,etc  |      Total  |
|  N° 1        |     22219, 23012, 23069, 23084  |  91384 |
|  N° 2        |      45303, 46096, 46153, 46168   | 183720 | 
|  N° 3        |    68387, 78691, 79016, 67231    | 226094 |
|  N° 4        |      101235, 109071, 109356 , 67231  | 319662 |
|  N° 5        |   131575, 132368, 132425, 132440  | 528808 |
|  Average     |                                | 269933.6   |


In the next tables we can compare the number of states obtained by turns be the first the states with many avalaible squares and the last the tables with less avalaible squares.

##### Machine plays first turn


| 3X3   |Min Max            |  Min Max Prunning   | Cut Off    (1)        |Cut Off    (2)     |
| :------: | :---------------: | :-----------------: | :-----------------:|:-----------------:|
|   9      |  549945 	       |   66453  	     |    2534 		  |      40936 	      | 
|   7      |   7331  	       |    1253  	     |    359   	  |     762  	      |   
|   5      |  197 	       |    42  	     |    325   	  |     66  	      |   
|   3      |  13  	       |    13  	     |    15    	  |      15  	      | 
|   1      |  1  	       |    1   	     |    1     	  |      1  	      |  
|  TOTAL   | 557487  	       |   67762  	     |    3234  	  |    41780 	      | 

##### Machine plays second turn


| 3X3      |Min Max            |  Min Max Prunning   | Cut Off   (1)      | Cut Off   (2)      |
| :------: | :---------------: | :-----------------: | :-----------------:| :-----------------:|
|   8      |  55504	       |   24802  	     |    3549 		  |     13965 	       | 
|   6      |   935  	       |    377  	     |    568   	  |    401   	       |   
|   4      |  50	       |    44  	     |    60    	  |       28           |
|   2      |  4  	       |     4  	     |    4    	          |      4    	       |
|  TOTAL   | 56493 	       |   25227  	     |    4181  	  |    14398  	       |  


For 4x4 tables we only use the algorithms of Min Max Cut Off because the rest of other algorithms take a long time to response.

##### Machine plays first turn

| 4X4      |  Cut Off (1)  |  Cut Off (2)   | 
| :------: | :---------------: | :-----------------: | 
|   15      |  41128 	       |   45518  	     |  
|   13      |  12251 	       |    17050  	     |  
|   11      |  7953	       |    3137 	     |    
|    9      |  3620 	       |    1197  	     | 
|   7      |  1793 	       |     674 	     | 
|   5      |  309	       |    99  	     | 
|   3      |  15 	       |    15 	             | 
|   1      |  1 	       |    1   	     | 
|  TOTAL   | 67070  	       |   67691 	     |


##### Machine plays second turn

| 4X4      |  Cut Off (1)  |  Cut Off (2)   | 
| :------: | :---------------: | :-----------------: | 
|   16      |  68929 	       |   14032  	     |  
|   14      |  17069  	       |    7052  	     |  
|   12      |  5455	       |    3862 	     |    
|   10      |  4937 	       |    1865  	     | 
|   8      |  356 	       |    1485 	     | 
|   6      |  924	       |    790  	     | 
|   4      |  56	       |    64 	             | 
|   2      |  4 	       |    4   	     | 
|  TOTAL   | 97730  	       |   29154  	     |




##### Machine plays first turn


| 5x5      |  Cut Off (1s)  |  Cut Off (2)   | 
| :------: | :---------------: | :-----------------: | 
|   25      |  22866 	       |   974  	     | 
|   23      |  19639 	       |   814  	     | 
|   21      |  15508 	       |   501  	     | 
|   19      |  22316 	       |   1545 	     | 
|   17      |  20957 	       |   2031  	     |  
|   15      |  14325  	       |    1829  	     |  
|   13      |  10021  	       |    737  	     | 
|   11      |  5479	       |    559 	     |    
|   9      |  1965 	       |    245  	     | 
|   7      |  759	       |    178 	     | 
|   5      |  139	       |    37  	     | 
|   3      |  15 	       |    15  	     | 
|   1      |   1 	       |    1   	     | 
|  TOTAL   | 133990  	       |   9466  	     |

##### Machine plays second turn

| 5x5      |  Cut Off (1)  |  Cut Off (2)   | 
| :------: | :---------------: | :-----------------: | 
|   24      |  547126 	       |   1741  	     | 
|   22      |  580542 	       |   1183  	     | 
|   20      |  617922 	       |   1145  	     | 
|   18      |  640462 	       |   1627 	     | 
|   16      |  652132 	       |   825  	     |  
|   14      |  668193  	       |    358  	     |  
|   12      |  676613  	       |    921  	     | 
|   10      |  679973	       |    95 	             |    
|   8      |  681017 	       |    52  	     | 
|   6      |  681241 	       |    82  	     | 
|   4      |  681295	       |    35  	     | 
|   2      |  681299	       |    4 	             | 
|  TOTAL   | 7787815  	       |   8068  	     |

##### Machine plays second turn


## What is the algorithm that takes more (less) and expands more (less) states? MinMax, MinMax + AlphaBeta Prunning or MinMaxCutoff?

#### 3x3
The Min max take 1.2 seg and 1.1 segs in average.

The states expanded is the worst when the pc take first turn.
The states expanded is the worst when the pc take second turn.

The Min max prunning take 0.22 segs and 0.1157 segs in average.

The states expanded is in the middle when the pc take first turn.
The states expanded is in the middle when the pc take second turn.

The cut off take 0.22 segs and 0.11 segs  in average.

The states expanded is in the best when the pc take first turn.
The states expanded is in the best when the pc take second turn.


Also we only obtain the time for 4x4 and 5x5 with the Cut Off algorithm.

#### 4x4
The first cut off take  1.4181 seg. and 1.0167 seg. in average.

The states expanded is the worst when the pc take first turn.
The states expanded is the worst when the pc take second turn.

The second cut off take  0.1712 seg. and 0.3959 seg. in average.

The states expanded is in the best when the pc take first turn.
The states expanded is in the best when the pc take second turn.

#### 5x5

The first cut off take  2.3286 seg. and 1.0474 seg. in average.

The states expanded is the worst when the pc take first turn.
The states expanded is the worst when the pc take second turn.

The second cut off take  0.0537 seg. and 0.0607 seg. in average.

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

