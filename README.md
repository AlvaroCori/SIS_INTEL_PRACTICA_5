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