
import pandas as pd
#TODO 1. Create a dictionary in this format:

alphaabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

guide_dic={row.letter : row.code for (index, row) in alphaabet_df.iterrows()}

#print(guide_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Type your name?").upper()

nato_l = [guide_dic[each] for each in name]
print(nato_l)




