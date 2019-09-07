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


def DDheatmap():
    # Make a csv file that only includes the daily double and clue location data.
    

    # Initialize each clue location.

    from copy import deepcopy
    
    # make a list of lists that shows the frequency of daily doubles at each clue location. Do the same for proportion of daily doubles at each clue location. 


    from matplotlib import colors

    # Note that Matplotlib reads coordinates like a cartesian coordinate where the $200 question in Category 2 would be read as 1,0, 
    # whereas numpy reads coordinates normally like 0,1. Hint: USE TRANPOSES!

    # Make a numpy array of the general list of lists that includes clues.

    # Make a transpose of that numpy array


    xaxis = [] # recall that there are 6 categories asked and 5 money values
    yaxis = []


    # We want to show all ticks...
  

    # ... and label them with the respective list entries


    # Rotate the tick labels and set their alignment.

    # Loop over data dimensions and create text annotations.

    # sort the list from highest to lowest to find where the daily doubles are commonly found.


def valueheatmap():
    # Follow the matplotlib heatmap documentation!
    # initialize all clue locations

    # Make a transpose of the numpy array

    xaxis = [] # recall that there are 6 categories asked and 5 money values
    yaxis = []
        


    # We want to show all ticks...


    # ... and label them with the respective list entries


    # Rotate the tick labels and set their alignment.

    # Loop over data dimensions and create text annotations.



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
    
    # print the most asked category, final jeopardy category, and most asked generalized jeopardy category



    #PLOTTING PORTION LIKE HW3
    with plt.xkcd():
        #create plots without the category "other"

        
        #create a barplot with axes general categories and frequency and a title. Give the barplot some color and edgecolor.
        #barplot


        #create a pieplot with labels for each general category, each slice being a different color and listing its percentage, have the starting angle be from 90 degrees on a unit circle
        #pieplot



def gamedynamics1(gamenum):  
    # Make a csv file that only includes the contestant's earnings after each question based on only the data in All Jeopardy Questions.csv. No webscraping!


def gamedynamics2(filename):
    # Choose any game whose dynamics you want to see! You can choose Game 8003 for example, which is linked below.
    # Create a line graph with a title, legend, and labels for each question number and money winnings for the 3 different players. Make sure to use the xkcd format.
    # ex: Game 8003 http://www.j-archive.com/showscores.php?game_id=6300
    # ex: Game 7973 http://www.j-archive.com/showscores.php?game_id=6266
    # write a csv file with all the entries. You can do this by copying the table to a Google Sheet and downloading it as a csv file.
    # Since these money values have commas in them, you must put double quotes around each element and have no spaces in between each element
        

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


def averagecluelength(rownumber):


def averageanswerlen():


def averageanswerlength(rownumber):


def averagecluewordlen():


def averageanswerwordlen():


def extremesentencelen(): # find the length of the longest and shortest sentence.


def numcharclue(character):


def numcharanswer(character):


def graph(): # make sure to use xkcd style


# Use this .csv to .txt converter to make a clue.txt file
def csv_to_txt():
    csv_file = input('Enter the name of your input file: ')
    txt_file = input('Enter the name of your output file: ')
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

def triplestumpernobuzz(): # find how many questions there were where nobody answered.


def triplestumperbuzz(): # find how many questions there were where nobody answered correctly and at least one person answered incorrectly.


def anyties(): # find how many total ties there are.


def winningties(): # find how many winning ties there are.

            
def extremewinstats(): # find the lowest and highest winning and 3rd place scores.


def winstats(): # find the median, mean, standard deviation, and variance in winning scores.


def winnames(): # find which names win the highest average and median scores. You can separate by first and last names.


def winmons(): # find which months give the highest and lowest average and median scores.


def podium(): # find the proportion of which each podium player (left, middle, right) wins.
    

def strong(): # find in how many games the second and third players had less than half of what the first player had, so the first player was guaranteed a win (assuming the first player doesn't bet badly)
    

def overthrown(): # find in how many games the first place player was overthrown after final jeopardy and ended up losing
    
       
def weak(): # find how many players were unable to move on to final jeopardy because they ended up with a negative score before finals
    

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