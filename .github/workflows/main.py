import pandas as pd 
from sklearn.model_selection import train_test_split

#loading the .dat file into a dataframe and separate into training and test set
with open('dailog_acts.dat') as file:
    dat= [row.strip().lower().split(maxsplit=1) for row in file]

data= pd.DataFrame(dat, columns=["dailog_act","utterance"])
training_data, test_data= train_test_split(data,test_size=0.15, random_state=42)

user_sentence= input().lower()
