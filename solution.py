board = [
   [],
   [],
   [],
   []
]

import random
from string import ascii_lowercase

for i in range(len(board)):
    rand_letters = random.choices(ascii_lowercase,k=4) #k is number of required rand_letters
    boggle_board = rand_letters

filename = "words_alpha.txt"

file = open(filename, "r")
raw = file.read()
word_list = []

def boggle_solver(board, x, y):

	string = []
	for i in range(len(raw)):
		string.append(board[x][y]).join('')
		print(string)
		word_list.append(string.count(raw));
		# word_list.append(boggle_solver(board, x+1, y+1))
		# word_list.append(boggle_solver(board, x, y+1)) 
		# word_list.append(boggle_solver(board, x-1, y+1)) 
		# word_list.append(boggle_solver(board, x+1, y)) 
		# word_list.append(boggle_solver(board, x-1, y)) 
		# word_list.append(boggle_solver(board, x+1, y-1)) 
		# word_list.append(boggle_solver(board, x, y-1)) 
		# word_list.append(boggle_solver(board, x-1, y-1))

		return word_list


print(boggle_solver(boggle_board, 1,1))
