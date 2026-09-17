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

#rule based function to decide a dialog act per sentence
def classification_dialog_sentence(sentence):
    if "thank" in sentence or "thank you" in sentence:
        return "thank you"
    if "noise" in sentence or "unintelligible" in sentence or "sil" in sentence or "cough" in sentence:
        return "null"
    if "ye"in sentence or "right" in sentence or "correct" in sentence:
        return "affirm"
    if "start" in sentence or "reset" in sentence:
        return "restart"
    if "wrong" in sentence or "dont want" in sentence or "not" in sentence:
        return "deny"
    if "repeat" in sentence or "back" in sentence or "again" in sentence:
        return "repeat" 
    if "no" in sentence:
        return "negate" 
    if "hello" in sentence:
        return "hello"
    if "it" in sentence and ("does" in sentence or "is" in sentence):
        return "confirm"
    if "could" in sentence or "address" in sentence or "number" in sentence or "phone" in sentence or "what" in sentence or "code" in sentence:
        return "request"
    if ("how" in sentence and "about" in sentence) or ("anything" in sentence and "else" in sentence):
        return "reqalts"
    if "bye" in sentence or "goodbye" in sentence:
        return "bye"
    elif "can" in sentence or "spanish" in sentence or "catalan" in sentence or "food" in sentence or "restaurant" in sentence or "town" in sentence or "spanish" in sentence:
        return "inform"
    elif "okay" in sentence or "kay" in sentence:
        return "ack"
    elif "more" in sentence:
        return "reqmore"

#function to test the accuracy of the assigned dialog act
def test_accuracy(test_data):
    correct_count= 0
    total_count=0
    for items in test_data:
        total_count+=1
        if classification_dialog_sentence(items[1])==items[0]:
            correct_count+=1
    return correct_count/total_count

print(test_accuracy(test_data))


