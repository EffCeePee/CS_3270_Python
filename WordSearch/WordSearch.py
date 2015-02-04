__author__ = 'Colton'

import sys
from pprint import pprint


class GameMatrix:
    def __init__(self):
        self.length = 0

    def setup_matrix(self, game_file):
        word_matrix_file = open(game_file)
        matrix = []
        index = 0
        line = word_matrix_file.readline().strip()

        self.length = line.__len__()
        while index < self.length:
            line = list(line)
            matrix.append(line)
            line = word_matrix_file.readline().strip()
            index += 1

        return matrix

    def get_length(self):
        return self.length


class Words:
    def __init__(self):
        self.size = 0
        self.game_file = None

    def get_word_list(self, size, game_file):
        self.size = size
        self.game_file = game_file
        temp_list = list(open(game_file))
        temp_list = temp_list[size:]
        word_list = []
        for x in temp_list:
            temp = x.strip('\n')
            if temp is not '':
                word_list.append(temp)
        return word_list


class Searches:
    def __init__(self, game_matrix, m_size):
        self.game_matrix = game_matrix
        self.m_size = m_size

    def find_start(self, word):
        a_word = list(word)
        b_found = False
        s_row = 0

        while s_row < self.m_size:
            s_col = 0
            while s_col < self.m_size and b_found is False:
                if a_word[0] == self.game_matrix[s_row][s_col]:
                    b_found, end_r, end_c = self.search(a_word, s_row, s_col)
                    s_col += 1
                else:
                    s_col += 1
            s_row += 1

        if b_found == True:
            return b_found, s_row, s_col, end_r, end_c
        else:
            end_r = None
            end_c = None
            return b_found, s_row, s_col, end_r, end_c

    def search(self, a_word, row, col):
        found = False
        for x in a_word:
            if x == self.game_matrix[row][col]:
                found = True
            else:
                found = False
                break

        return found, row, col



game = GameMatrix()
words = Words()
matrix_file = sys.argv[1]
word_matrix = game.setup_matrix(matrix_file)
matrix_size = game.get_length()
words = words.get_word_list(matrix_size, matrix_file)
Searches = Searches(word_matrix, matrix_size)

for word in words:
    found, start_col, start_row, end_row, end_col = Searches.find_start(word)
    print(word)
    print(str(start_col) + ' ' + str(start_row) + ' ' + str(end_row) + ' ' + str(end_col))