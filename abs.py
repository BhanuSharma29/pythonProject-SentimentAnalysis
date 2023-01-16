import pandas as pd
x= pd.read_csv('/Users/bhanu/Desktop/ABSS/KEY18_22C.csv')
import re
import matplotlib.pyplot as plt


frequency = {}
document_text = open('/Users/bhanu/Desktop/ABSS/KEY18_22C.csv', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

blacklisted = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
               "again",
               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", 'the', 'and', 'for', 'that',
               'which']

for word in match_pattern:
    if word not in blacklisted:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))

most_frequent_count = most_frequent.keys()

for words in most_frequent_count:
    print(words, most_frequent[words])
x= words
y= most_frequent[x]
fig,ax1 = plt.subplots(221)
fig3, axes = plt.subplots(nrows=5,ncols=1)

fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()



