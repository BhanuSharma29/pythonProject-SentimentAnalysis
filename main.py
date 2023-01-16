


# Cleaning Text Steps
#1) Create a text file and take text from it
#2) Convert a letter into lowercase ('Apple' is not equal to 'apple'
# 3) Remove punctuations like .,? etc (Hi ! This is buildwithpython.)

# import string
#text = open('read.text',encoding='utf-8').read()
# lower_case = text.lower()

# in the below cleantext line inside maketrans meaning is as follows
# str1: Specifies the list of characters that need to be replaced
# str2: Specifies the list of characters with which the characters need to be replaced.
#str3: Specifies the list of characters that needs to be deleted
#cleaned_text =lower_case.translate(str.maketrans('','', string.punctuation))
#print(cleaned_text)

import string
from collections import Counter
##from typing import List, Any
import matplotlib.pyplot as plt
text = open('read.text',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text =lower_case.translate(str.maketrans('','', string.punctuation))
tokenized_words = cleaned_text.split()
##print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now",]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
## print(final_words)




# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#- open the emotion file
# -Loop through each line and clear it
# - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list --- emotion_list[]
#3) Finally count each emotion in the emotion list


emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)

w= Counter(emotion_list)
print(w)

fig,ax1 = plt.subplots()  # subplot that has figure and its axis
ax1.bar(w.keys(),w.values()) # to create the actual graph
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()


