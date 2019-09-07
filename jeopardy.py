# THIS ASSIGNMENT INTEGRATES CREATING CSV FILES, MATPLOTLIB VISUALIZATIONS, AND NATURAL LANGUAGE PROCESSING, POSSIBLE MACHINE LEARNING
# Have your model guess what some test set of jeopardy questions are/what their categories are

# heatmap of how often each square is picked first, taking argument square
# CREATE THE JEOPARDY TABLE WITH CLICK ABILITY
# USE NATURAL LANGUAGE PROCESSING TO GENERATE JEOPARDY QUESTIONS

import csv
import string
import matplotlib.pyplot as plt
import numpy as np

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#

from collections import *

def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []

#
# write_to_csv shows how to write that format from a list of rows...
#
def write_to_csv( list_of_rows, filename ):
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        count = 0
        for row in list_of_rows:
            count += 1
            filewriter.writerow(row ) 
            # filewriter.writerow( {row + ":" + str(list_of_rows[row])} ) # must be treated as list because csv returns a list
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")


LQA = readcsv("All Jeopardy Questions.csv") # list of questions and answers

# Make a csv file that only includes the clues.
clue = []
for i in range(len(LQA[1:])):
    clues = LQA[i][14]
    clue += [clues]
write_to_csv(clue, "clue.csv")

def DDheatmap():
    dailydoubles = []
    for i in range(len(LQA[1:])):
        DD = LQA[i][17]
        if DD == '1':
            dailydoubles += [LQA[i][8]]
    write_to_csv(dailydoubles, "dailydouble.csv")
    LODD = open("dailydouble.txt", "r") # r for read
    _1_1 = 0
    _1_2 = 0
    _1_3 = 0
    _1_4 = 0
    _1_5 = 0
    _2_1 = 0
    _2_2 = 0
    _2_3 = 0
    _2_4 = 0
    _2_5 = 0
    _3_1 = 0
    _3_2 = 0
    _3_3 = 0
    _3_4 = 0
    _3_5 = 0
    _4_1 = 0
    _4_2 = 0
    _4_3 = 0
    _4_4 = 0
    _4_5 = 0
    _5_1 = 0
    _5_2 = 0
    _5_3 = 0
    _5_4 = 0
    _5_5 = 0
    _6_1 = 0
    _6_2 = 0
    _6_3 = 0
    _6_4 = 0
    _6_5 = 0
    for row in LODD:
        if "_ 1 _ 1" in row:
            _1_1 += 1
        elif "_ 1 _ 2" in row:
            _1_2 += 1
        elif "_ 1 _ 3" in row:
            _1_3 += 1
        elif "_ 1 _ 4" in row:
            _1_4 += 1
        elif "_ 1 _ 5" in row:
            _1_5 += 1
        elif "_ 2 _ 1" in row:
            _2_1 += 1
        elif "_ 2 _ 2" in row:
            _2_2 += 1
        elif "_ 2 _ 3" in row:
            _2_3 += 1
        elif "_ 2 _ 4" in row:
            _2_4 += 1
        elif "_ 2 _ 5" in row:
            _2_5 += 1
        elif "_ 3 _ 1" in row:
            _3_1 += 1
        elif "_ 3 _ 2" in row:
            _3_2 += 1
        elif "_ 3 _ 3" in row:
            _3_3 += 1
        elif "_ 3 _ 4" in row:
            _3_4 += 1
        elif "_ 3 _ 5" in row:
            _3_5 += 1
        elif "_ 4 _ 1" in row:
            _4_1 += 1
        elif "_ 4 _ 2" in row:
            _4_2 += 1
        elif "_ 4 _ 3" in row:
            _4_3 += 1
        elif "_ 4 _ 4" in row:
            _4_4 += 1
        elif "_ 4 _ 5" in row:
            _4_5 += 1
        elif "_ 5 _ 1" in row:
            _5_1 += 1
        elif "_ 5 _ 2" in row:
            _5_2 += 1
        elif "_ 5 _ 3" in row:
            _5_3 += 1
        elif "_ 5 _ 4" in row:
            _5_4 += 1
        elif "_ 5 _ 5" in row:
            _5_5 += 1
        elif "_ 6 _ 1" in row:
            _6_1 += 1
        elif "_ 6 _ 2" in row:
            _6_2 += 1
        elif "_ 6 _ 3" in row:
            _6_3 += 1
        elif "_ 6 _ 4" in row:
            _6_4 += 1
        elif "_ 6 _ 5" in row:
            _6_5 += 1
    
    from copy import deepcopy
    allspots = [_1_1] + [_1_2] + [_1_3] + [_1_4] + [_1_5] + [_2_1] + [_2_2] + [_2_3] + [_2_4] + [_2_5] + [_3_1] + [_3_2] + [_3_3] + [_3_4] + [_3_5] + [_4_1] + [_4_2] + [_4_3] + [_4_4] + [_4_5] + [_5_1] + [_5_2] + [_5_3] + [_5_4] + [_5_5] + [_6_1] + [_6_2] + [_6_3] + [_6_4] + [_6_5]
    _1 = [_1_1] + [_1_2] + [_1_3] + [_1_4] + [_1_5]
    _2 = [_2_1] + [_2_2] + [_2_3] + [_2_4] + [_2_5]
    _3 = [_3_1] + [_3_2] + [_3_3] + [_3_4] + [_3_5]
    _4 = [_4_1] + [_4_2] + [_4_3] + [_4_4] + [_4_5]
    _5 = [_5_1] + [_5_2] + [_5_3] + [_5_4] + [_5_5]
    _6 = [_6_1] + [_6_2] + [_6_3] + [_6_4] + [_6_5]
    m = 13594
    _1m = [round(_1_1/m,4)] + [round(_1_2/m,4)] + [round(_1_3/m,4)] + [round(_1_4/m,4)] + [round(_1_5/m,4)]
    _2m = [round(_2_1/m,4)] + [round(_2_2/m,4)] + [round(_2_3/m,4)] + [round(_2_4/m,4)] + [round(_2_5/m,4)]
    _3m = [round(_3_1/m,4)] + [round(_3_2/m,4)] + [round(_3_3/m,4)] + [round(_3_4/m,4)] + [round(_3_5/m,4)]
    _4m = [round(_4_1/m,4)] + [round(_4_2/m,4)] + [round(_4_3/m,4)] + [round(_4_4/m,4)] + [round(_4_5/m,4)]
    _5m = [round(_5_1/m,4)] + [round(_5_2/m,4)] + [round(_5_3/m,4)] + [round(_5_4/m,4)] + [round(_5_5/m,4)]
    _6m = [round(_6_1/m,4)] + [round(_6_2/m,4)] + [round(_6_3/m,4)] + [round(_6_4/m,4)] + [round(_6_5/m,4)]

    from matplotlib import colors

    # Note that Matplotlib reads coordinates like a cartesian coordinate where the $200 question in Category 2 would be read as 1,0, 
    # whereas numpy reads coordinates normally like 0,1. Hint: USE TRANPOSES!

    frequencies = np.array([_1, _2, _3, _4, _5, _6])
    tfrequencies = np.transpose(frequencies) # the transpose
    freqperts = np.array([_1m,_2m,_3m,_4m,_5m,_6m])
    tfreqperts = np.transpose(freqperts) # the transpose
    # print("tFREQUENCIES")
    # print(tfrequencies)
    xaxis = ["Category 1","Category 2","Category 3","Category 4","Category 5","Category 6"] # recall that there are 6 categories asked and 5 money values
    yaxis = ['$200','$400','$600','$800','$1000']
        
    fig, ax = plt.subplots()
    # cmap = colors.ListedColormap(["navy", "royalblue", "lightsteelblue", "peachpuff", "salmon", "darkred"])    
    im = ax.imshow(tfrequencies)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(xaxis)))
    ax.set_yticks(np.arange(len(yaxis)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(xaxis)
    ax.set_yticklabels(yaxis)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Loop over data dimensions and create text annotations.
    for i in range(len(xaxis)): # indexes row
        for j in range(len(yaxis)): # indexes col
            text = ax.text(i, j, tfrequencies[j, i], ha="center", va="center", color="w")

    cbar = ax.figure.colorbar(im, ax=ax)

    ax.set_title("Frequency Proportions of where Daily Doubles are Found")
    fig.tight_layout()
    plt.show()

    allspotscopy = deepcopy(allspots) # create a deepcopy of allspots
    print("ALLSPOTS")
    print(allspots)
    # sort the list from highest to lowest to find where the daily doubles are commonly found.
    allspots.sort(reverse = True)
    print("DESCENDING")
    print(allspots)
    print("COPY")
    print(allspotscopy)
    descendingallspotsindices = [allspotscopy.index(x) for x in allspots]
    print("DESCENDING INDICES")
    print(descendingallspotsindices)
    # The index of the max value of jeopardy daily doubles is index 3 of the list, which is at the location _1_4
    # from highest to lowest, the daily doubles are commonly found in _1_3, _3_4, _4_4, _5_4, _1_2, _3_3 ...

def valueheatmap():
    J_1_1 = 0
    J_1_2 = 0
    J_1_3 = 0
    J_1_4 = 0
    J_1_5 = 0
    J_2_1 = 0
    J_2_2 = 0
    J_2_3 = 0
    J_2_4 = 0
    J_2_5 = 0
    J_3_1 = 0
    J_3_2 = 0
    J_3_3 = 0
    J_3_4 = 0
    J_3_5 = 0
    J_4_1 = 0
    J_4_2 = 0
    J_4_3 = 0
    J_4_4 = 0
    J_4_5 = 0
    J_5_1 = 0
    J_5_2 = 0
    J_5_3 = 0
    J_5_4 = 0
    J_5_5 = 0
    J_6_1 = 0
    J_6_2 = 0
    J_6_3 = 0
    J_6_4 = 0
    J_6_5 = 0
    DJ_1_1 = 0
    DJ_1_2 = 0
    DJ_1_3 = 0
    DJ_1_4 = 0
    DJ_1_5 = 0
    DJ_2_1 = 0
    DJ_2_2 = 0
    DJ_2_3 = 0
    DJ_2_4 = 0
    DJ_2_5 = 0
    DJ_3_1 = 0
    DJ_3_2 = 0
    DJ_3_3 = 0
    DJ_3_4 = 0
    DJ_3_5 = 0
    DJ_4_1 = 0
    DJ_4_2 = 0
    DJ_4_3 = 0
    DJ_4_4 = 0
    DJ_4_5 = 0
    DJ_5_1 = 0
    DJ_5_2 = 0
    DJ_5_3 = 0
    DJ_5_4 = 0
    DJ_5_5 = 0
    DJ_6_1 = 0
    DJ_6_2 = 0
    DJ_6_3 = 0
    DJ_6_4 = 0
    DJ_6_5 = 0
    for i in range(2, len(LQA[3:])):
        #print(LQA[i][-1], LQA[i][-2], LQA[i][-3])
        if LQA[i][-1] != '' and LQA[i][-2] != '' and LQA[i][-3] != '' and LQA[i-1][-1] != '' and LQA[i-1][-2] != '' and LQA[i-1][-3] != '':
            # print('a')
            # print(LQA[i-1][-2])
            # print('b')
            # print(LQA[i][-2])
            # print('c')
            # print(float(LQA[i-1][-2]))
            # print('d')
            # print(float(LQA[i][-2]))
            if float(LQA[i-1][-1]) - float(LQA[i][-1]) != 0.0:
                change = float(LQA[i][-1]) - float(LQA[i-1][-1])
            elif float(LQA[i-1][-2]) - float(LQA[i][-2]) != 0.0:
                change = float(LQA[i][-2]) - float(LQA[i-1][-2])
            elif float(LQA[i-1][-3]) - float(LQA[i][-3]) != 0.0:
                change = float(LQA[i][-3]) - float(LQA[i-1][-3])
                if LQA[i][8] == 'J_1_1':
                    J_1_1 += change
                elif LQA[i][8] == 'J_1_2':
                    J_1_2 += change
                elif LQA[i][8] == 'J_1_3':
                    J_1_3 += change
                elif LQA[i][8] == 'J_1_4':
                    J_1_4 += change
                elif LQA[i][8] == 'J_1_5':
                    J_1_5 += change
                elif LQA[i][8] == 'J_2_1':
                    J_2_1 += change
                elif LQA[i][8] == 'J_2_2':
                    J_2_2 += change
                elif LQA[i][8] == 'J_2_3':
                    J_2_3 += change
                elif LQA[i][8] == 'J_2_4':
                    J_2_4 += change
                elif LQA[i][8] == 'J_2_5':
                    J_2_5 += change
                elif LQA[i][8] == 'J_3_1':
                    J_3_1 += change
                elif LQA[i][8] == 'J_3_2':
                    J_3_2 += change
                elif LQA[i][8] == 'J_3_3':
                    J_3_3 += change
                elif LQA[i][8] == 'J_3_4':
                    J_3_4 += change
                elif LQA[i][8] == 'J_3_5':
                    J_3_5 += change
                elif LQA[i][8] == 'J_4_1':
                    J_4_1 += change
                elif LQA[i][8] == 'J_4_2':
                    J_4_2 += change
                elif LQA[i][8] == 'J_4_3':
                    J_4_3 += change
                elif LQA[i][8] == 'J_4_4':
                    J_4_4 += change
                elif LQA[i][8] == 'J_4_5':
                    J_4_5 += change
                elif LQA[i][8] == 'J_5_1':
                    J_5_1 += change
                elif LQA[i][8] == 'J_5_2':
                    J_5_2 += change
                elif LQA[i][8] == 'J_5_3':
                    J_5_3 += change
                elif LQA[i][8] == 'J_5_4':
                    J_5_4 += change
                elif LQA[i][8] == 'J_5_5':
                    J_5_5 += change
                elif LQA[i][8] == 'J_6_1':
                    J_6_1 += change
                elif LQA[i][8] == 'J_6_2':
                    J_6_2 += change
                elif LQA[i][8] == 'J_6_3':
                    J_6_3 += change
                elif LQA[i][8] == 'J_6_4':
                    J_6_4 += change
                elif LQA[i][8] == 'J_6_5':
                    J_6_5 += change
                if LQA[i][8] == 'DJ_1_1':
                    DJ_1_1 += change
                elif LQA[i][8] == 'DJ_1_2':
                    DJ_1_2 += change
                elif LQA[i][8] == 'DJ_1_3':
                    DJ_1_3 += change
                elif LQA[i][8] == 'DJ_1_4':
                    DJ_1_4 += change
                elif LQA[i][8] == 'DJ_1_5':
                    DJ_1_5 += change
                elif LQA[i][8] == 'DJ_2_1':
                    DJ_2_1 += change
                elif LQA[i][8] == 'DJ_2_2':
                    DJ_2_2 += change
                elif LQA[i][8] == 'DJ_2_3':
                    DJ_2_3 += change
                elif LQA[i][8] == 'DJ_2_4':
                    DJ_2_4 += change
                elif LQA[i][8] == 'DJ_2_5':
                    DJ_2_5 += change
                elif LQA[i][8] == 'DJ_3_1':
                    DJ_3_1 += change
                elif LQA[i][8] == 'DJ_3_2':
                    DJ_3_2 += change
                elif LQA[i][8] == 'DJ_3_3':
                    DJ_3_3 += change
                elif LQA[i][8] == 'DJ_3_4':
                    DJ_3_4 += change
                elif LQA[i][8] == 'DJ_3_5':
                    DJ_3_5 += change
                elif LQA[i][8] == 'DJ_4_1':
                    DJ_4_1 += change
                elif LQA[i][8] == 'DJ_4_2':
                    DJ_4_2 += change
                elif LQA[i][8] == 'DJ_4_3':
                    DJ_4_3 += change
                elif LQA[i][8] == 'DJ_4_4':
                    DJ_4_4 += change
                elif LQA[i][8] == 'DJ_4_5':
                    DJ_4_5 += change
                elif LQA[i][8] == 'DJ_5_1':
                    DJ_5_1 += change
                elif LQA[i][8] == 'DJ_5_2':
                    DJ_5_2 += change
                elif LQA[i][8] == 'DJ_5_3':
                    DJ_5_3 += change
                elif LQA[i][8] == 'DJ_5_4':
                    DJ_5_4 += change
                elif LQA[i][8] == 'DJ_5_5':
                    DJ_5_5 += change
                elif LQA[i][8] == 'DJ_6_1':
                    DJ_6_1 += change
                elif LQA[i][8] == 'DJ_6_2':
                    DJ_6_2 += change
                elif LQA[i][8] == 'DJ_6_3':
                    DJ_6_3 += change
                elif LQA[i][8] == 'DJ_6_4':
                    DJ_6_4 += change
                elif LQA[i][8] == 'DJ_6_5':
                    DJ_6_5 += change
    J_1 = [J_1_1] + [J_1_2] + [J_1_3] + [J_1_4] + [J_1_5]
    J_2 = [J_2_1] + [J_2_2] + [J_2_3] + [J_2_4] + [J_2_5]
    J_3 = [J_3_1] + [J_3_2] + [J_3_3] + [J_3_4] + [J_3_5]
    J_4 = [J_4_1] + [J_4_2] + [J_4_3] + [J_4_4] + [J_4_5]
    J_5 = [J_5_1] + [J_5_2] + [J_5_3] + [J_5_4] + [J_5_5]
    J_6 = [J_6_1] + [J_6_2] + [J_6_3] + [J_6_4] + [J_6_5]
    DJ_1 = [DJ_1_1] + [DJ_1_2] + [DJ_1_3] + [DJ_1_4] + [DJ_1_5]
    DJ_2 = [DJ_2_1] + [DJ_2_2] + [DJ_2_3] + [DJ_2_4] + [DJ_2_5]
    DJ_3 = [DJ_3_1] + [DJ_3_2] + [DJ_3_3] + [DJ_3_4] + [DJ_3_5]
    DJ_4 = [DJ_4_1] + [DJ_4_2] + [DJ_4_3] + [DJ_4_4] + [DJ_4_5]
    DJ_5 = [DJ_5_1] + [DJ_5_2] + [DJ_5_3] + [DJ_5_4] + [DJ_5_5]
    DJ_6 = [DJ_6_1] + [DJ_6_2] + [DJ_6_3] + [DJ_6_4] + [DJ_6_5]
    values = np.array([J_1, J_2, J_3, J_4, J_5, J_6, DJ_1, DJ_2, DJ_3, DJ_4, DJ_5, DJ_6])
    print(values)
    tvalues = np.transpose(values) # the transpose
    print(tvalues)
    # print("tvalues")
    # print(tvalues)
    xaxis = ["Category J1","Category J2","Category J3","Category J4","Category J5","Category J6, Category DJ1","Category DJ2","Category DJ3","Category DJ4","Category DJ5","Category DJ6"] # recall that there are 6 categories asked and 5 money values
    yaxis = ['$200','$400','$600','$800','$1000', '$1200', '$1400', '$1600', '$1800', '$2000']
        
    fig, ax = plt.subplots()
    # cmap = colors.ListedColormap(["navy", "royalblue", "lightsteelblue", "peachpuff", "salmon", "darkred"])    
    im = ax.imshow(tvalues)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(xaxis)))
    ax.set_yticks(np.arange(len(yaxis)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(xaxis)
    ax.set_yticklabels(yaxis)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Loop over data dimensions and create text annotations.
    for i in range(len(xaxis)): # indexes row
        for j in range(len(yaxis)): # indexes col
            text = ax.text(j, i, tvalues[i, j], ha="center", va="center", color="w") # axis 0 = rows, axis 1 = cols

    cbar = ax.figure.colorbar(im, ax=ax)

    ax.set_title("Frequency Proportions of where Daily Doubles are Found")
    fig.tight_layout()
    plt.show()


# using the 319K+ Q&A Jeopardy CSV Dataset to determine number of unique categories, 
# determine how commonly each category, final jeopardy category, and general category is asked through a dictionary, 
# get the max values of categories by doing max(a.values())
# make csv files of categories, final jeopardy categories, and general categories
#
def removekey(d, key): # removes key from dictionary, use this so you make a copy of a dictionary and don't change the original dictionary
    r = dict(d)
    del r[key]
    return r

# warning: running on the whole 319K+ rows file on the jeopardy() function can have a runtime of minutes. We suggest you try on a portion of the dataset while you still write your code.
def jeopardy():
    #WORKING WITH CSV FILES PORTION LIKE HW2
    fj = {}
    d = {}
    newd = {} # dictionary of general categories
    LOC = [] # list of categories
    #make sure not to include the first row in the csv file that has the whole dataset because those are just titles of each column
    for row in LQA[1:]: 
        category = str(row[13])
        round = str(row[8])
        if "FJ" in round:
            if category not in fj: 
                fj[category] = 1
            else:
                fj[category] += 1
        if category not in LOC:
            LOC += [category]
            d[category] = 1
        else:
            d[category] += 1
    #make 2 new csv files, one for categories and finaljeopardy categories
    write_to_csv(d, "categories.csv")
    write_to_csv(fj, "finaljeopardy.csv")
    newd['history'] = 0
    newd['politics'] = 0
    newd['movies/tv'] = 0
    newd['other'] = 0
    newd['stem'] = 0
    newd['food'] = 0
    newd['religion'] = 0
    newd['mythology'] = 0
    newd['music'] = 0
    newd['geography'] = 0
    newd['literature'] = 0
    newd['art'] = 0
    newd['economics'] = 0
    newd['sports'] = 0
    #make all elements in the dictionary lowercase
    lowerd = dict((key.lower(), value) for key, value in d.items())
    for row in lowerd:
        if 'history' in row or 'century' in row or 'queen' in row or 'ages' in row or 'war' in row or 'nation' in row or 'historic' in row or 'before they' in row or 'explorer' in row or '60' in row or '70' in row or '80' in row or '90' in row or '1960' in row or '1950' in row or '1970' in row or '1980' in row or '1990' in row or '2000' in row:
            newd['history'] += 1 
        elif 'politic' in row or 'cabinet' in row or 'election' in row or 'empire' in row or 'leader' in row or 'supreme court' in row or 'presidency' in row or 'senator' in row or 'presidents' in row or 'king' in row or 'royal' in row or 'government' in row:
            newd['politics'] += 1
        elif 'celebs' in row or "afi's" in row or 'celebrities' in row or 'cinema' in row or 'episode' in row or 'drama' in row or 'comedy' in row or 'tv' in row or 'fashion' in row or 'pop' in row or 'beatles' in row or 'famous' in row or 'movie' in row or 'broadway' in row or 'film' in row or 'television' in row or 'oscars' in row or 'hollywood' in row or 'actor' in row or 'actress' in row:
            newd['movies/tv'] += 1
        elif 'science' in row or 'internet' in row or 'machine' in row or 'flower' in row or 'tree' in row or 'element' in row or 'online' in row or 'planet' in row or 'site' in row or 'weather' in row or 'astro' in row or 'number' in row or 'invent' in row or 'nature' in row or 'anatomy' in row or 'doctor' in row or 'medic' in row or 'animal' in row or 'geometry' in row or 'zoology' in row or 'algebra' in row or 'trigonometry' in row or 'calculus' in row or 'statistic' in row or 'physics' in row or 'tech' in row or 'chemistry' in row or 'math' in row or 'engineering' in row or 'biology' in row or 'computer' in row:
            newd['stem'] += 1
        elif 'food' in row or 'fruit' in row or 'candy' in row or 'vegetable' in row or 'beer' in row or 'drink' in row or 'eateries' in row or 'restaurant' in row or 'cuisine' in row:
            newd['food'] += 1
        elif 'religion' in row or 'religious' in row or 'commandment' in row or 'church' in row or 'cathedral' in row or 'testament' in row or 'pope' in row or 'christian' in row or 'biblical' in row or 'bible' in row or 'holy' in row or 'saint' in row:
            newd['religion'] += 1
        elif 'myth' in row or 'greek' in row or 'roman' in row:
            newd['mythology'] += 1
        elif 'music' in row or 'jazz' in row or 'album' in row or 'ipod' in row or 'sing' in row or 'song' in row or 'lyric' in row or 'grammy' in row or 'tune' in row or 'composer' in row or 'dance' in row or 'opera' in row or 'musical' in row or 'instrument' in row or 'orchestra' in row or 'band' in row or 'choir' in row or 'mozart' in row or 'chopin' in row or 'bach' in row or 'beethoven' in row:
            newd['music'] += 1
        elif 'map' in row or 'college' in row or 'british' in row or 'states' in row or 'university' in row or 'canada' in row or 'france' in row or 'england' in row or 'germany' in row or 'china' in row or 'italy' in row or 'spain' in row or 'russia' in row or 'asia' in row or 'city' in row or 'town' in row or 'tour' in row or 'land' in row or 'travel' in row or 'place' in row or 'island' in row or 'mountain' in row or 'lake' in row or 'river' in row or 'sea' in row or 'world' in row or 'europe' in row or 'africa' in row or 'australia' in row or 'antarctica' in row or 'america' in row or 'countries' in row or 'volcano' in row or 'landmark' in row or 'geography' in row or 'flag' in row or 'geographic' in row or 'capital' in row or 'cartography' in row or 'continent' in row:
            newd['geography'] += 1
        elif 'literature' in row or 'philosophy' in row or 'pulitzer' in row or 'lingo' in row or 'page' in row or 'bestseller' in row or 'haiku' in row or 'etymology' in row or 'dictionary' in row or 'literary' in row or 'anagram' in row or 'novel' in row or 'shakespeare' in row or 'fiction' in row or 'poet' in row or 'crossword' in row or 'homophone' in row or 'bestseller' in row or 'author' in row or 'ends in' in row or 'starts with' in row or 'book' in row or 'vocab' in row or 'rhyme' in row or 'acronym' in row or 'simile' in row or 'metaphor' in row:
            newd['literature'] += 1
        elif 'art' in row or 'exhibit' in row or 'ballet' in row or 'paint' in row or 'theater' in row or 'publication' in row or 'magazine' in row or 'news' in row or 'museum' in row or 'draw' in row:
            newd['art'] += 1
        elif 'econ' in row or 'business' in row or 'advert' in row or 'transaction' in row or 'company' in row or 'gambl' in row or 'brand' in row or 'money' in row or 'job' in row or 'industry' in row or 'finance' in row or 'financial' in row or 'fortune' in row or 'stock' in row or 'money' in row or 'currency' in row:
            newd['economics'] += 1
        elif 'athlet' in row or 'ball' in row or 'race' in row or 'nba' in row or 'nfl' in row or 'espn' in row or 'sport' in row or 'football' in row or 'tennis' in row or 'olympic' in row or 'soccer' in row or 'baseball' in row or 'swim' in row or 'archery' in row or 'wrestling' in row:
            newd['sports'] += 1
        else:
            newd['other'] += 1
    
    #find the most asked category, final jeopardy category, and most asked generalized jeopardy category
    for key, value in d.items():
        if max(d.values()) == value:
            maxdcategory = key
    for key, value in fj.items():
        if max(fj.values()) == value:
            maxfjcategory = key
    for key, value in newd.items():
        if max(newd.values()) == value:
            maxnewdcategory = key

    #print("THIS IS D")
    #print(d)
    #print("THIS IS FJ")
    #print(fj)
    #print("THIS IS NEWD")
    #print(newd)
    print("The most asked category, " + str(maxdcategory) + " was asked " + str(max(d.values())) + " times.")
    print("The most asked final jeopardy category, " + str(maxfjcategory) + " was asked " + str(max(fj.values())) + " times.")
    print("The most asked generalized jeopardy category, " + str(maxnewdcategory) + " was asked " + str(max(newd.values())) + " times.")
    print("Number of categories: " + str(len(d)))
    
    partialcategories = dict(list(d.items())) 
    partialfj = dict(list(fj.items()))
    partialnewd = dict(list(newd.items()))


    #PLOTTING PORTION LIKE HW3
    with plt.xkcd():
        #create plots without the category "other"
        newnewd = removekey(newd, 'other')
        
        #create a barplot with axes general categories and frequency and a title. Give the barplot some color and edgecolor.
        #barplot
        x = [x for x in newnewd] # gives back the keys in newd
        y = [y for y in newnewd.values()]
        plt.xlabel("General Categories")
        plt.ylabel("Frequency")
        plt.title("Frequency of General Jeopardy Categories")
        plt.bar(x,y,color='blue',edgecolor='purple')
        plt.show()

        #create a pieplot with labels for each general category, each slice being a different color and listing its percentage, have the starting angle be from 90 degrees on a unit circle
        #pieplot
        sizes = [100*newnewd[element]/len(newnewd) for element in newnewd]
        cols = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'indigo', 'magenta', 'brown', 'gray', 'black', 'white', 'pink']
        plt.pie(sizes, (0,0,0,0,0,0,0,0,0.1,0,0,0,0),labels = [element for element in newnewd], colors = cols, autopct = '%1.1f%%', startangle = 90)
        plt.show()


def gamedynamics1(gamenum):  
    # Make a csv file that only includes the contestant's earnings after each question.
    game = []
    for i in range(1, len(LQA[1:])):
        if LQA[i][3] == str(gamenum): # for different games
            games = [LQA[i][-3], LQA[i][-2], LQA[i][-1]]
            game += [games]
    scores = write_to_csv(game, str(gamenum)+".csv")
    scoresread = readcsv(scores)
    print(scoresread)
    with plt.xkcd():
        qnum = list(range(61))
        counter = 0
        cont1 = []
        cont2 = []
        cont3 = []
        for row in scoresread: # make sure to exclude the first row which has the contestants' names
            for element in row:
                if element != '': # note that some elements in the row are empty strings
                    counter += 1
                    if element.startswith('-'): # account for the negative sign if there's negative money accumulated
                        element = float(element.replace(',','')[2:])
                        if counter%3 == 1: # cannot do row.index(element) of because element won't be in row 
                            cont1 += [element]
                        elif counter%3 == 2:
                            cont2 += [element]
                        elif counter%3 == 0:
                            cont3 += [element] 
                    else:
                        element = float(element.replace(',','')[1:])
                        if counter%3 == 1: # cannot do row.index(element) of because element won't be in row 
                            cont1 += [element]
                        elif counter%3 == 2:
                            cont2 += [element]
                        elif counter%3 == 0:
                            cont3 += [element]                
        print(cont1)
        print(len(cont1))
        print(cont2)
        print(len(cont2))
        print(cont3)
        print(len(cont3))
        plt.plot(qnum,cont1,label='contestant 1')
        plt.plot(qnum,cont2,label='contestant 2')
        plt.plot(qnum,cont3,label='contestant 3')
        plt.title("Game Dynamics")
        plt.xlabel("Question Number")
        plt.ylabel("Money Winnings ($)")
        plt.legend()
        plt.show()


def gamedynamics2(filename):
    # Choose any game whose dynamics you want to see! You can choose Game 8003 for example, which is linked below.
    # Create a line graph with a title, legend, and labels for each question number and money winnings for the 3 different players. Make sure to use the xkcd format.
    # ex: Game 8003 http://www.j-archive.com/showscores.php?game_id=6300
    # ex: Game 7973 http://www.j-archive.com/showscores.php?game_id=6266
    # write a csv file with all the entries. You can do this by copying the table to a Google Sheet and downloading it as a csv file.
    # Since these money values have commas in them, you must put double quotes around each element and have no spaces in between each element
        #ax = plt.axes()
        #ax.grid()
        #plt.axis('equal')
    with plt.xkcd():
        scores = readcsv(filename)
        qnum = list(range(61))
        counter = 0
        cont1 = []
        cont2 = []
        cont3 = []
        for row in scores[1:]: # make sure to exclude the first row which has the contestants' names
            for element in row:
                if element != '': # note that some elements in the row are empty strings
                    counter += 1
                    if element.startswith('-'): # account for the negative sign if there's negative money accumulated
                        element = float(element.replace(',','')[2:])
                        if counter%3 == 1: # cannot do row.index(element) of because element won't be in row 
                            cont1 += [element]
                        elif counter%3 == 2:
                            cont2 += [element]
                        elif counter%3 == 0:
                            cont3 += [element] 
                    else:
                        element = float(element.replace(',','')[1:])
                        if counter%3 == 1: # cannot do row.index(element) of because element won't be in row 
                            cont1 += [element]
                        elif counter%3 == 2:
                            cont2 += [element]
                        elif counter%3 == 0:
                            cont3 += [element]                
        print(cont1)
        print(len(cont1))
        print(cont2)
        print(len(cont2))
        print(cont3)
        print(len(cont3))
        plt.plot(qnum,cont1,label='contestant 1')
        plt.plot(qnum,cont2,label='contestant 2')
        plt.plot(qnum,cont3,label='contestant 3')
        plt.title("Game Dynamics")
        plt.xlabel("Question Number")
        plt.ylabel("Money Winnings ($)")
        plt.legend()
        plt.show()


# Natural Language Processing Portion
## Import all of the libraries and data that we will need.
import nltk
import textblob

from textblob import TextBlob
from textblob import Word

from nltk.corpus import names  # see the note on installing corpora
from nltk.corpus import opinion_lexicon

import random
import math

from sklearn.feature_extraction import DictVectorizer
import sklearn
import sklearn.tree
from sklearn.metrics import confusion_matrix

import statistics
from statistics import median
from statistics import mean
from statistics import mode
# from statistics import harmonic_mean
# from statistics import median_low
# from statistics import median_high
# from statistics import median_grouped # Return the median of grouped continuous data, calculated as the 50th percentile, using interpolation
# ex) median_low([1, 3, 5, 7]) # 3
# ex) median_high([1, 3, 5, 7]) # 5
# ex) median_grouped([1, 3, 3, 5, 7], interval=1) # 3.25
# ex) median_grouped([1, 3, 3, 5, 7], interval=2) # 3.5
# from statistics import pstdev # population is 1/n. sample is 1/n-1
# from statistics import pvariance
from statistics import stdev
from statistics import variance

plt.close('all')
fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

# 1st and 2nd nums are reciprocals of the nums, so 3 takes up 1/3 the space. 3-3 would be 1/3 the space vertically, 1/2 the space horizontally, subplot1
# ax1 = fig.add_subplot(3-3)
# ax2 = fig.add_subplot(-12)
# ax3 = fig.add_subplot(413)
ax1 = plt.subplot2grid((6,3), (0,2), rowspan=2, colspan=3) # first tuple shows in the grid how many rows and cols to have. Thus, all subplots must have the same first tuple.
ax2 = plt.subplot2grid((6,3), (2,1), rowspan=3, colspan=2) # second tuple shows position of plot
ax3 = plt.subplot2grid((6,3), (5,0), rowspan=1, colspan=1) # rowspan and colspan must be less than or equal to numbers in first tuple
x,y = create_plots()
# ax1.plot(x,y)
x,y = create_plots() # must redo this for each subplot
ax2.plot(x,y)
x,y = create_plots()
# ax3.plot(x,y)
plt.tight_layout() # use this with subplot2grid
# plt.show()

def averagecluelen():
    numwords = []
    for row in LQA[1:]:
        TB = textblob.TextBlob(row[14])
        numword = 0
        for word in TB.words:
            numword += 1
        numwords += [numword]
    numwords = tuple(numwords)
    print("MEDIAN: " + str(median(numwords)))
    print("MODE: " + str(mode(numwords)))
    print("STDEV: " + str(stdev(numwords)))
    return mean(numwords)

def averagecluelength(rownumber):
    numwords = []
    TB = textblob.TextBlob(LQA[rownumber][14])
    numword = 0
    for word in TB.words:
        numword += 1
        numwords += [numword]
    numwords = tuple(numwords)
    #print("MEDIAN: " + str(median(numwords)))
    return mean(numwords)

def averageanswerlen():
    numwords = []
    for row in LQA[1:]:
        TB = textblob.TextBlob(row[15])
        numword = 0
        for word in TB.words:
            numword += 1
        numwords += [numword]
    numwords = tuple(numwords)
    print("MEDIAN: " + str(median(numwords)))
    print("MODE: " + str(mode(numwords)))
    print("STDEV: " + str(stdev(numwords)))
    return mean(numwords)

def averageanswerlength(rownumber):
    numwords = []
    TB = textblob.TextBlob(row[rownumber][15])
    numword = 0
    for word in TB.words:
        numword += 1
    numwords += [numword]
    numwords = tuple(numwords)
    #print("MEDIAN: " + str(median(numwords)))
    return mean(numwords)

def averagecluewordlen():
    wordlengths = []
    for row in LQA[1:]:
        TB = textblob.TextBlob(row[14])
        for word in TB.words:
            wordlengths += [len(word)]
    wordlengths = tuple(wordlengths)
    print("MEDIAN: " + str(median(wordlengths)))
    print("MODE: " + str(mode(wordlengths)))
    print("STDEV: " + str(stdev(wordlengths)))
    print("VARIANCE: " + str(variance(wordlengths)))
    return mean(wordlengths)

def averageanswerwordlen():
    wordlengths = []
    for row in LQA[1:]:
        TB = textblob.TextBlob(row[15])
        for word in TB.words:
            wordlengths += [len(word)]
    wordlengths = tuple(wordlengths)
    print("MEDIAN: " + str(median(wordlengths)))
    print("MODE: " + str(mode(wordlengths)))
    print("STDEV: " + str(stdev(wordlengths)))
    print("VARIANCE: " + str(variance(wordlengths)))
    return mean(wordlengths)    

def extremesentencelen(): # find the length of the longest and shortest sentence.
    sentlengths = []
    for i in range(len(LQA[1:])):
        rawtext = LQA[i][14]
        TB = textblob.TextBlob( rawtext )
        words = 0
        for word in TB.words:
            words += 1
        sentlengths += [words]
    return max(sentlengths), min(sentlengths)

def numcharclue(character):
    count = 0
    for row in LQA[1:]:
        rawtext = row[14]
        TB = textblob.TextBlob( rawtext )
        # from here, you can use TB.words and TB.sentences...
        for char in TB:
            if char == character:
                count += 1
    return count

def numcharanswer(character):
    count = 0
    for row in LQA[1:]:
        rawtext = row[14]
        TB = textblob.TextBlob( rawtext )
    # from here, you can use TB.words and TB.sentences...
        for char in TB:
            if char == character:
                count += 1
    return count

def graph(): # make sure to use xkcd style
    with plt.xkcd():
        num = 0
        for i in range(len(LQA[1:50])):
            n = len(LQA[1:])
            num += 1
            X = num # each user gets points on the x-axis
            Y = averagecluelength(i)
            color = np.random.rand()
            plt.scatter(X,Y, c=color, alpha=.5)
            #T = np.arctan2(Y,X)

        plt.xlim(0,len(LQA[1:50]))#, plt.xticks([])
        plt.ylim(0,1-1)#, plt.yticks([])
        plt.xlabel("Row")
        plt.ylabel("Average Word Length in Letters")
        plt.title("Average Word Length in Letters of each Row")

        plt.show()

# Use this .csv to .txt converter to make a clue.txt file
def csv_to_txt():
    csv_file = input('Enter the name of your input file: ')
    txt_file = input('Enter the name of your output file: ')
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

def triplestumpernobuzz(): # find how many questions there were where nobody answered.
    triplestumpers = []
    for row in LQA[1:]:
        if row[18] == '0.0' and row[19] == '0.0' and row[20] == '0.0':
            triplestumpers += [row[14]]
    print("There are " + str(len(triplestumpers)) + " no buzz in triple stumpers!")
    return triplestumpers

def triplestumperbuzz(): # find how many questions there were where nobody answered correctly and at least one person answered incorrectly.
    triplestumpers = []
    for row in LQA[1:]:
        if row[18] < '0.0' and row[19] <= '0.0' and row[20] <= '0.0':
            triplestumpers += [row[14]]
        elif row[18] <= '0.0' and row[19] < '0.0' and row[20] <= '0.0':
            triplestumpers += [row[14]]
        elif row[18] <= '0.0' and row[19] <= '0.0' and row[20] < '0.0':
            triplestumpers += [row[14]]
    print("There are " + str(len(triplestumpers)) + " buzz in triple stumpers!")
    return triplestumpers

def anyties(): # find how many total ties there are.
    ties = []
    for i in range(len(LQA[1:])):
        scores = [LQA[i][-3], LQA[i][-2], LQA[i][-1]]
        if LQA[i][4] != LQA[i + 1][4]: # if the game is different
            if LQA[i][-3] == LQA[i][-2]: # ties
                ties += [LQA[i][-3]]
            elif LQA[i][-3] == LQA[i][-1]:
                ties += [LQA[i][-3]]
            elif LQA[i][-2] == LQA[i][-1]:
                ties += [LQA[i][-1]]
    print("There are " + str(len(ties)) + " ties.")
    return ties

def winningties(): # find how many winning ties there are.
    ties = []
    for i in range(len(LQA[1:])):
        scores = [LQA[i][-3], LQA[i][-2], LQA[i][-1]]
        if LQA[i][4] != LQA[i + 1][4]: # if the game is different
            if LQA[i][-3] == max(scores) and LQA[i][-3] == LQA[i][-2]: # ties
                ties += [LQA[i][-3]]
            elif LQA[i][-3] == max(scores) and LQA[i][-3] == LQA[i][-1]:
                ties += [LQA[i][-3]]
            elif LQA[i][-1] == max(scores) and LQA[i][-2] == LQA[i][-1]:
                ties += [LQA[i][-1]]
    print("There are " + str(len(ties)) + " winning ties.")
    return ties
            
def extremewinstats(): # find the lowest and highest winning and 3rd place scores.
    winningscores = []
    thirdscores = []
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '':
            scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
            if LQA[i][4] != LQA[i + 1][4]: # if the game is different
                winningscores += [max(scores)]
                thirdscores += [min(scores)]
    print("The lowest winning score is " + str(min(winningscores)))
    print("The highest winning score is " + str(max(winningscores)))
    print("The highest 3rd place score is " + str(max(thirdscores)))
    print("The lowest 3rd place score is " + str(min(thirdscores)))

def winstats(): # find the median, mean, standard deviation, and variance in winning scores.
    winningscores = []
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '':
            scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
            if LQA[i][4] != LQA[i + 1][4]: # if the game is different
                winningscores += [max(scores)]
    print("The median winning score is " + str(median(winningscores)))
    print("The mean winning score is " + str(mean(winningscores)))
    print("The standard deviation in winning scores is " + str(stdev(winningscores)))
    print("The variance in winning scores is " + str(variance(winningscores)))

def winnames(): # find which names win the highest average and median scores. You can separate by first and last names.
    thatname = {}
    namecount = {}
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '':
            if LQA[i][4] != LQA[i + 1][4]: # if the game is different
                for j in range(3):
                    temp = LQA[i][j+5]
                    if ' ' in temp:
                        name = temp[:temp.index(' ')] # first name
                        namecount[name] = 0
                        if name not in thatname:
                            if name in LQA[i][5]: # is contestant 1
                                thatname[name] = float(LQA[i][-3])
                                namecount[name] += 1
                            elif name in LQA[i][6]: # is contestant 2
                                thatname[name] = float(LQA[i][-2])
                                namecount[name] += 1
                            elif name in LQA[i][7]: # is contestant 1
                                thatname[name] = float(LQA[i][-1])
                                namecount[name] += 1
                        else:
                            if name in LQA[i][5]: # is contestant 1
                                thatname[name] += float(LQA[i][-3])
                                namecount[name] += 1
                            elif name in LQA[i][6]: # is contestant 2
                                thatname[name] += float(LQA[i][-2])
                                namecount[name] += 1
                            elif name in LQA[i][7]: # is contestant 1
                                thatname[name] += float(LQA[i][-1])
                                namecount[name] += 1
                for k in range(3):
                    temp = LQA[i][j+5]
                    if ' ' in temp:
                        name = temp[1+temp.index(' '):] # last name
                        namecount[name] = 0
                        if name not in thatname:
                            if name in LQA[i][5]: # is contestant 1
                                thatname[name] = float(LQA[i][-3])
                                namecount[name] += 1
                            elif name in LQA[i][6]: # is contestant 2
                                thatname[name] = float(LQA[i][-2])
                                namecount[name] += 1
                            elif name in LQA[i][7]: # is contestant 1
                                thatname[name] = float(LQA[i][-1])
                                namecount[name] += 1
                        else:
                            if name in LQA[i][5]: # is contestant 1
                                thatname[name] += float(LQA[i][-3])
                                namecount[name] += 1
                            elif name in LQA[i][6]: # is contestant 2
                                thatname[name] += float(LQA[i][-2])
                                namecount[name] += 1
                            elif name in LQA[i][7]: # is contestant 1
                                thatname[name] += float(LQA[i][-1])
                                namecount[name] += 1
    for name in thatname:
        thatname[name] = thatname[name]/namecount[name]
    return "The name that on average wins the most money is " + str(max(thatname, key=thatname.get))

def winmons(): # find which months give the highest and lowest average and median scores.
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    oct = []
    nov = []
    dec = []
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '':
            scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
            if LQA[i][4] != LQA[i + 1][4]: # if the game is different
                if LQA[i][4][5:7] == '01':
                    jan += [max(scores)]
                    jana = mean(jan)
                    janm = median(jan)
                elif LQA[i][4][5:7] == '02':
                    feb += [max(scores)]
                    feba = mean(feb)
                    febm = median(feb)
                elif LQA[i][4][5:7] == '03':
                    mar += [max(scores)]
                    mara = mean(mar)
                    marm = median(mar)
                elif LQA[i][4][5:7] == '04':
                    apr += [max(scores)]
                    apra = mean(apr)
                    aprm = median(mar)
                elif LQA[i][4][5:7] == '05':
                    may += [max(scores)]
                    maya = mean(may)
                    maym = median(may)
                elif LQA[i][4][5:7] == '06':
                    jun += [max(scores)]
                    juna = mean(jun)
                    junm = median(jun)
                elif LQA[i][4][5:7] == '07':
                    jul += [max(scores)]
                    jula = mean(jul)
                    julm = median(jul)
                elif LQA[i][4][5:7] == '08':
                    aug += [max(scores)]
                    auga = mean(aug)
                    augm = median(aug)
                elif LQA[i][4][5:7] == '09':
                    sep += [max(scores)]
                    sepa = mean(sep)
                    sepm = median(sep)
                elif LQA[i][4][5:7] == '10':
                    oct += [max(scores)]
                    octa = mean(oct)
                    octm = median(oct)
                elif LQA[i][4][5:7] == '11':
                    nov += [max(scores)]
                    nova = mean(nov)
                    novm = median(nov)
                elif LQA[i][4][5:7] == '12':
                    dec += [max(scores)]
                    deca = mean(dec)
                    decm = median(dec)
    allmonsa = [jana] + [feba] + [mara] + [apra] + [maya] + [juna] + [jula] + [auga] + [sepa] + [octa] + [nova] + [deca]
    allmonsm = [janm] + [febm] + [marm] + [aprm] + [maym] + [junm] + [julm] + [augm] + [sepm] + [octm] + [novm] + [decm]
    print("The highest average score of a winner in any particular month is " + str(max(allmonsa)) + " in " + "Month " + str(1 + allmonsa.index(max(allmonsa))) + ".") 
    print("The highest median score of a winner in any particular month is " + str(max(allmonsm)) + " in " +  "Month " + str(1 + allmonsm.index(max(allmonsm))) + ".")
    print("The lowest average score of a winner in any particular month is " + str(min(allmonsa)) + " in " + "Month " + str(1 + allmonsa.index(min(allmonsa))) + ".") 
    print("The lowest median score of a winner in any particular month is " + str(min(allmonsm)) + " in " + "Month " + str(1 + allmonsm.index(min(allmonsm))) + ".")

def podium(): # find the proportion of which each podium player (left, middle, right) wins.
    first = []
    second = []
    third = []
    ties = 0
    numgames = 5574
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '':
            scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
            if LQA[i][3] != LQA[i + 1][3]: # if the game is different
                if float(LQA[i][-1]) == max(scores) and float(LQA[i][-2]) != max(scores) and float(LQA[i][-3]) != max(scores):
                    first += [LQA[i][-1]]
                elif float(LQA[i][-2]) == max(scores) and float(LQA[i][-1]) != max(scores) and float(LQA[i][-3]) != max(scores):
                    second += [LQA[i][-2]]
                elif float(LQA[i][-3]) == max(scores) and float(LQA[i][-1]) != max(scores) and float(LQA[i][-2]) != max(scores):
                    third += [LQA[i][-3]]
                else:
                    ties += 1
    print("The first (left) podium has a win percentage of: ")
    print(len(first)/numgames)
    print("The second (middle) podium has a win percentage of ")
    print(len(second)/numgames)
    print("The third (right) podium has a win percentage of ")
    print(len(third)/numgames)
    print("There were " + str(ties) + " ties.")

def strong(): # find in how many games the second and third players had less than half of what the first player had, so the first player was guaranteed a win (assuming the first player doesn't bet badly)
    strongs = 0
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '' and LQA[i-1][-3] != '' and LQA[i-1][-2] != '' and LQA[i-1][-1] != '':
            scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
            if LQA[i][3] != LQA[i + 1][3]: # if the game is different
                if float(LQA[i-1][-3]) < .5 * max(scores) and float(LQA[i-1][-2]) < .5 * max(scores):
                    strongs += 1
                elif float(LQA[i-1][-3]) < .5 * max(scores) and float(LQA[i-1][-1]) < .5 * max(scores):
                    strongs += 1
                elif float(LQA[i-1][-2]) < .5 * max(scores) and float(LQA[i-1][-1]) < .5 * max(scores):
                    strongs += 1
    return strongs

def overthrown(): # find in how many games the first place player was overthrown after final jeopardy and ended up losing
    overthrowns = 0
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '' and LQA[i-1][-3] != '' and LQA[i-1][-2] != '' and LQA[i-1][-1] != '':
            if LQA[i][3] != LQA[i + 1][3]: # if the game is different
                prescores = [float(LQA[i-1][-3]), float(LQA[i-1][-2]), float(LQA[i-1][-1])]
                scores = [float(LQA[i][-3]), float(LQA[i][-2]), float(LQA[i][-1])]
                prefjwinnerindex = prescores.index(max(prescores))
                postfjwinnerindex = scores.index(max(scores))
                if prefjwinnerindex != postfjwinnerindex:
                    overthrowns += 1
    return "There were " + str(overthrowns) + " players overthrown after final jeopardy."
       
def weak(): # find how many players were unable to move on to final jeopardy because they ended up with a negative score before finals
    weaks = 0
    for i in range(1, len(LQA[1:])):
        if LQA[i][-3] != '' and LQA[i][-2] != '' and LQA[i][-1] != '' and LQA[i-1][-3] != '' and LQA[i-1][-2] != '' and LQA[i-1][-1] != '':
            if LQA[i][3] != LQA[i + 1][3]: # if the game is different
                if float(LQA[i][-1]) < 0:
                    weaks += 1
                elif float(LQA[i][-2]) < 0:
                    weaks += 1
                elif float(LQA[i][-3]) < 0:
                    weaks += 1
    return "There were " + str(weaks) + " players who had negative scores before the final jeopardy round, so they did not participate."

# Question Text Generator
# Taken from https://nbviewer.jupyter.org/gist/yoavg/d761-3dfde26184--339

def train_char_lm(fname, order=4): # fname = filename
    f = open(fname, 'r')
    data = f.read()
    lm = defaultdict(Counter)
    pad = "~" * order # pad the data with leading ~ so that we also learn how to start
    data = pad + data
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]
    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    return outlm

from random import random

def generate_letter(lm, history, order):
        history = history[-order:]
        dist = lm[history]
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: 
                return c

def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in range(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)

# order = 6+ seems to give more Englishy words but does not make much sense
# lm = train_char_lm("clue.txt", order=7)
# print(generate_text(lm, 7))

    

# if __name__ == "__main__":
#     main()

# main()

# Some exercises in game/betting/gambling strategies: Prisoner's Dilemma, Crush, Two-Thirds Rule, Stratton’s Dilemma, Jeek’s Rule, Faith Law, Boyd’s Rule, Coryat scores, Shore’s conjecture. Given an example of each scenario, identify which/what betting strategy
# Definition of terms: http://www.j-archive.com/help.php#coryatscore
# Shore’s conjecture explained: http://thefinalwager.com/shores/

# In the two-thirds scenario, a trailing player with a score at least two-thirds the score of the leading player going into Final Jeopardy! should wager between $0 (venusian) and 
# 3*(own score) - 2*(leader's score) (martian), according to the Two-thirds Rule. Wagering more than this actually lowers the trailing player's odds of winning by 
# reducing the number of favorable outcomes in the payoff matrix from 2/4 to 1/4. An interesting side-effect of the Two-thirds Rule is that a bet to cover by the leader 
# renders inconsequential the trailing player's Final Jeopardy! response: whether the two-thirds trailing player gets right or misses Final Jeopardy!, 
# he or she will win if the leader misses it (presuming that a third player is not a factor).

# The three-quarters scenario is a special case of the two-thirds scenario in which a trailing player with a score at least three-quarters the score of the leading player going into 
# Final Jeopardy! safely can, and therefore should, wager to cover a $0 bet by the leader. According to the Three-quarters Rule, the trailing player should wager between 
# (leader's score - own score)--or, if affordable, (leader's score - own score + $1)--(venusian) and 3*(own score) - 2*(leader's score) (martian).

# The four-fifths scenario is a special case of the two-thirds scenario in which a trailing player with a score at least four-fifths the score of the leading player going into 
# Final Jeopardy! safely can, and therefore should, wager to beat the leader's maximum safe bet of the difference between scores with a bet of twice the difference between the 
# two scores, without losing the double stumper against a shut-out bet by the leader. According to the Four-fifths Rule, the trailing player should wager between 
# (2*(leader's score - own score) + $1) (venusian) and 3*(own score) - 2*(leader's score) (martian).

# $6900 - $10800 - $ 14900 (Stratton’s Dilemma)
# $5,200 - $5,200 - $5,200 (Jeek’s Rule)
# $9,200-$8,600-$4,000, $10,400-$9,800-$4,600 (Faith Love)
# $11,800 $14,700 $16,200 (Boyd’s Rule)
# $18,200	$14,000	$3,800 (Weak Shore's)
# $16,600	$15,000	$1,700 (Intermediate Shore's)
# $19,400	$4,200	$17,800 (Strong Shore's)"""