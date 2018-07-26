
import random
dice = [
    [['AAEEGN'],['ELRTTY'],['AOOTTW'],['ABBJOO']],
    [['EHRTVW'],['CIMOTU'],['DISTTY'],['EIOSST']],
    [['DELRVY'],['ACHOPS'],['HIMNQU'],['EEINSU']],
    [['EEGHNW'],['AFFKPS'],['HLNNRZ'],['DEILRX']]
    ]

for i in range(len(dice)):
    for j in range(len(dice[i])):
        secure_random = random.SystemRandom()
        letters = secure_random.choice(dice[i][j][0])
        print(letters)

board = []
for n in range(4):
	board.append([])
#print(board)
for x in range(len(board)):
	for i in range(4):
		board[x].append([secure_random.choice(dice[i][j][0])])
	print(board[x])
print(board)

#This gets a random 4x4 board each time. Now we have to find out how to solve the boggle.
#Commented out below is my failed attempt.


# def boggle_solver(board, x, y):

# 	string = []
# 	for i in range(len(raw)):
# 		string.append(board[x][y]).join('')
# 		print(string)
# 		word_list.append(string.count(raw));
# 		# word_list.append(boggle_solver(board, x+1, y+1))
# 		# word_list.append(boggle_solver(board, x, y+1)) 
# 		# word_list.append(boggle_solver(board, x-1, y+1)) 
# 		# word_list.append(boggle_solver(board, x+1, y)) 
# 		# word_list.append(boggle_solver(board, x-1, y)) 
# 		# word_list.append(boggle_solver(board, x+1, y-1)) 
# 		# word_list.append(boggle_solver(board, x, y-1)) 
# 		# word_list.append(boggle_solver(board, x-1, y-1))

# 		return word_list


# print(boggle_solver(boggle_board, 1,1))
