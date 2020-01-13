# -*- coding: utf-8 -*-

import pdb
import random

#import json
#with open('klc.json', encoding='utf8') as review_file:
#    raw_file = json.load(review_file)


class Review:
    ''' uses the parameters selected by the user in class Win to create a 
    review list '''
    def __init__(self, raw_file, first_num, last_num):

        self.raw_file = raw_file
        self.first_num = first_num
        self.last_num = last_num + 1 #

        self.rev_list = []


    def select_elements(self):
        '''uses the parameters selected by the user in class Win to create a 
        review list'''
        first = self.first_num
        last = self.last_num
        self.rev_list = [self.raw_file[str(i)] for i in range(first, last)]
        #for i in range(self.first_num, self.last_num):
        #   self.rev_list.append(self.raw_file[str(i)])

        return self.rev_list

    def shuffle(self):#, selection):
        '''TODO'''
        if not self.rev_list:
            self.rev_list = self.select_elements()

        if len(self.rev_list) == 1:
            self.end_review()

        
        a_word = random.choice(self.rev_list)

        self.rev_list.remove(a_word)

        return a_word

    def end_review(self):
        '''take the last element from review and finish the session'''
        if len(self.rev_list) == 1:
            a_word = random.choice(self.rev_list)
            self.rev_list.remove(a_word)
            #print(a_word, 'end_review')
            return a_word
        else:
            return 'congrats'


# test = Review(raw_file,1,5)
# print(test.shuffle())
# print(test.shuffle())
# print(test.shuffle())
# print(test.shuffle())
# print(test.shuffle())