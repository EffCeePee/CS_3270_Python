#__author__ = 'Colton'

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
    def __init__(self, search_words, g_matrix):
        self.search_words = search_words
        self.g_matrix = g_matrix

    def find_words(self):
        o_index = 0
        index = 0
        for s in self.search_words:
            for x in self.g_matrix[index][o_index]:
                print(x)
            s_word = list(self.search_words[o_index])
            print(s_word)
            o_index += 1



game = GameMatrix()
words = Words()
matrix_file = sys.argv[1]
word_matrix = game.setup_matrix(matrix_file)
matrix_size = game.get_length()
words = words.get_word_list(matrix_size, matrix_file)
searches = Searches(words, word_matrix)
searches.find_words()