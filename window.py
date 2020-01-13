import tkinter as tk
#from tkinter import ttk, messagebox
#import random
import json
import os
import reviewing as rev
#import calendar

class Win(tk.Tk):
    '''TODO'''
    def __init__(self):
        super().__init__()
        self.title('ReWoc')

        self.show_available_json()
        self.options_frame()
        

    def show_available_json(self):
        '''shows a list with all files from the folder voc_json'''
        this_dir = os.getcwd()
        files_in_dir = os.listdir(this_dir+'\\voc_json')
        self.json_file = tk.StringVar(self)

        list_of_json = tk.OptionMenu(self, self.json_file, *files_in_dir)

        self.json_file.set(files_in_dir[0]) # default value
        #self.json_file.set("select one from the list")
        list_of_json.pack()

    def select_json_to_review(self):
        '''load selected json as a dict to be used after in self.star_review'''
        selection = self.json_file.get()

        with open(selection, encoding='utf8') as review_file:
            raw_file = json.load(review_file)

        return raw_file

    def options_frame(self):
        '''frame tha contains the entry for first and last number, reverse
        checkbox and the button 'Go' to start the review'''

        self.frame_options = tk.Frame(self, padx=5)
        self.frame_options.pack()

        self.from_label = tk.Label(self.frame_options, text='From')
        self.from_label.grid(row=0, column=0, padx=5, pady=5)

        self.from_entry = tk.Entry(self.frame_options, width='5')
        self.from_entry.grid(row=0, column=1)

        self.to_label = tk.Label(self.frame_options, text='To')
        self.to_label.grid(row=0, column=2)

        self.to_entry = tk.Entry(self.frame_options, width='5')
        self.to_entry.grid(row=0, column=3)

        self.go_button = tk.Button(self.frame_options, text='Go!', command=self.start_review)
        self.go_button.grid(row=0, column=4, padx=10)

        self.isreverse = tk.BooleanVar()

        self.reverse = tk.Checkbutton(self.frame_options, text='Reverse', pady=5, variable=self.isreverse)
        self.reverse.grid(row=0, column=5)


    def start_review(self):
        '''gets the user input and selected json to instantiate the class Review
        from reviewing.py'''

        first_num = self.from_entry.get()
        last_num = self.to_entry.get()

        first_num = int(first_num)
        last_num = int(last_num)

        raw_file = self.select_json_to_review()

        review_session = rev.Review(raw_file, first_num, last_num)

        ############################################
        test = review_session.shuffle()

        print(test)
        ############################################


    def bottom_frame(self):
        '''frame that contains L1 and L2 labels with 'show', 'next', and 'hide'
        buttons'''
        pass

if __name__ == "__main__":

    root = Win()
    root.mainloop()
    #b.pack(root, side="top", fill="both", expand=True)
