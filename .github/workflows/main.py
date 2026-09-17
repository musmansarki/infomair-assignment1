import pandas as pd 
from sklearn.model_selection import train_test_split
from collections import Counter

#loading the .dat file and separate into training and test set
with open('dailog_acts.dat') as file:
    dat= [row.strip().lower().split(maxsplit=1) for row in file]

training_data, test_data= train_test_split(dat,test_size=0.15, random_state=42)

#creating bag of words per dailog act with a counter for the number of words per bag
bag_of_words_dict= dict()
for items in training_data:
    dialog_label= items[0]
    dialog_utterance= items[1].split()
    if dialog_label not in bag_of_words_dict:
        bag_of_words_dict[dialog_label]=Counter()
    bag_of_words_dict[dialog_label].update(dialog_utterance)
print(bag_of_words_dict)