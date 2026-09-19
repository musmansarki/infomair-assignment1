import pandas as pd 
from sklearn.model_selection import train_test_split
from collections import Counter
import re

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



nationalities=["spanish","catelan","italian","indian","lebanese", "swedish", "japanese", "mexican", "hungarian","russian", "greek", "irish",
                "cuban", "australian","danish", "welsh", "swiss","singaporean", "polish", "indonesian"
               "afghan", "malaysian", "english", "moroccan", "jamaican", "eritrean","scottish","romanian","german","austrian","brazilian"
               "thai","chinese","vietnamese","korean","turkish","portugese","french","british","american","tailand",
               "asian", "oriental","european", "mediterranean", "international", "african","caribbean","cantonese","polynesian",
                "corsica", "basque", "scandinavian", "tuscan","persian","venetian","belgian","australian" ]

#function to classify sentence with a dialog_act label
def classification(sentence):
    if re.search(r"\b(start again|reset|restart|start over)\b", sentence):
        return "restart"
    if re.search(r"\b(wrong|dont want|not)\b", sentence):
        return "deny"
    if re.search(r"\b(repeat|back|again)\b", sentence):
        return "repeat"
    if re.search(r"\b(how about|anything else|what about|next)\b", sentence):
        return "reqalts"
    if re.search(r"\bno\b", sentence):
        return "negate"
    if re.search(r"\b(ye|yeah|yea|perfect|right|correct|yes)\b", sentence):
            return "affirm"
    if re.search(r"\b(hello|hi|halo)\b", sentence):
        return "hello"
    if re.search(r"\b(could|address|number|what|phone number|post code|postcode|may i have|whats the|can i have the|where|price range)\b",sentence):
        return "request"
    if re.search(r"\b(it does|it is|does it|is it|do they serve|is there a .* restaurant|is that .* food)\b", sentence):
        return "confirm"
    if re.search(r"\b(thank|thank you|thanks)\b",sentence):
            return "thank you"
    if re.search(r"\b(bye|goodbye|good bye)\b", sentence):
        return "bye"
    if re.search(rf"\b({'|'.join(nationalities)}|can|food|eartrain|center|matter|moderate|dont care|restaurant|town|moderately|looking|north|west|centre|east|south|any|cheap|seafood|expensive|bistro)\b", sentence):
        return "inform"
    if re.search(r"\b(okay|kay)\b",sentence):
        return "ack"
    if re.search(r"\bmore\b", sentence):
        return "reqmore"
    else: return "null"

#function to test the accuracy of the assigned dialog act
def test_accuracy(test_data):
    correct_count= 0
    total_count=0
    for items in test_data:
        total_count+=1
        if classification(items[1])==items[0]:
            correct_count+=1
    return correct_count/total_count

print(test_accuracy(test_accuracy))


