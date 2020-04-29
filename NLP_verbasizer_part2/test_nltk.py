from textblob import TextBlob
from textblob import Word
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

import random

# nltk.download('punkt')
# SENT_DETECTOR = nltk.data.load('tokenizers/punkt/english.pickle')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('tagsets')
# nltk.download('brown')

sentences = "There was nothing so VERY  to take out of it, 123 and burning rabbit-hole 8988under " \
            "the hedge.   on, Alice started to her" \
            "quite natural); but when the"

# sentences = "This is my cat. I love playing. I love eating, I hate running, that is a  beautiful game and i am trying to play still"

words = word_tokenize(sentences)


# Spell check word by word
# for i in sentences:
#     sentence = sentences.split(' ')
#
# for i in sentence:
#     word = Word(i).correct()
#     print(word, end=' ')
#
# print()

### Handling Characters & Numbers in the sentences


all_character_list = ['`', '~', '!', '@', '#','$', '%', '^', '&','*', '(', ')', '-', '_', '+', '{', '}', '[', ']',
                  '|', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/', '=']


# Loop to know the list of all the symbolic characters in a sentence

actual_characters = list()
numbers_used = list()

for characters in sentences:
    if characters in all_character_list:
        actual_characters += characters

final_character_list = list(dict.fromkeys(actual_characters))

print(f'Sentence has the characters {final_character_list}') ## removing duplicate characters from sentences

# Loop to replace all the symbols with empty spaces

for i in all_character_list:
    if i in sentences:
        sentences = sentences.replace(i, ' ')

numbers_used += re.findall(r'[0-9]+', sentences)

print(f'Sentence contains numbers : {numbers_used}')
print(f'Sentence without symbols : {sentences}')

### Tokenizing the sentences to words for processing

sent_list = sent_tokenize(sentences)

test = str()

stop_words = set(stopwords.words("english"))

filtered_stop_words = [word for word in words if word not in stop_words ]

print(f'Sentence contains stop words which had been filtered : {filtered_stop_words}')

## Tagging with parts of speech for analysis and taken over by rules

# all_pos = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT','POS','PRP','PRP$',
#            'RB','RBR','RBS','RP','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']

# dict_1 = {}
# dict_2 = {}

for i in sent_list:
    pos_tagged_words = nltk.pos_tag(word_tokenize(i))

# dict_1 = dict(pos_tagged_words)
#
# dict2 = { values: [item] for item, values in dict_1.items()}

# for x in pos_tagged_words:
#      # dict_1 = dict_1(pos_tagged_words[x][1] = pos_tagged_words[x][0])
#     print(pos_tagged_words[x][0])

# print('pos_tagged_words dict 1 is :', dict_1)
# print('pos_tagged_words dict 2 is :', dict_2)


# print(sent_list)
# print(filtered_words)

CC_list = []
CD_list = []
DT_list = []
EX_list = []
FW_list = []
IN_list = []
JJ_list = []
JJR_list = []
JJS_list = []
LS_list = []
MD_list = []
NN_list = []
NNS_list = []
NNP_list = []
NNPS_list = []
PDT_list = []
POS_list = []
PRP_list = []
PRP2_list = []
RB_list = []
RBR_list = []
RBS_list = []
RP_list = []
TO_list = []
UH_list = []
VB_list = []
VBD_list = []
VBG_list = []
VBN_list = []
VBP_list = []
VBZ_list = []
WDT_list = []
WP_list = []
WP2_list = []
WRB_list = []
sentence_pos_list = []

for x in range(0,len(pos_tagged_words)):

    if pos_tagged_words[x][1] == "CC":
        sentence_pos_list.append("CC")
        CC_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "CD":
        sentence_pos_list.append("CD")
        CD_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "DT":
        sentence_pos_list.append("DT")
        DT_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "EX":
        sentence_pos_list.append("EX")
        EX_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "FW":
        sentence_pos_list.append("FW")
        FW_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "IN":
        sentence_pos_list.append("IN")
        IN_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "JJ":
        sentence_pos_list.append("JJ")
        JJ_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "JJR":
        sentence_pos_list.append("JJR")
        JJR_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "JJS":
        sentence_pos_list.append("JJS")
        JJS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "LS":
        sentence_pos_list.append("LS")
        LS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "MD":
        sentence_pos_list.append("MD")
        MD_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "NN":
        sentence_pos_list.append("NN")
        NN_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "NNS":
        sentence_pos_list.append("NNS")
        NNS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "NNP":
        sentence_pos_list.append("NNP")
        NNP_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "NNPS":
        sentence_pos_list.append("NNPS")
        NNPS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "PDT":
        sentence_pos_list.append("PDT")
        PDT_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "POS":
        sentence_pos_list.append("POS")
        POS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "PRP":
        sentence_pos_list.append("PRP")
        PRP_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "PRP$":
        sentence_pos_list.append("PRP$")
        PRP2_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "RB":
        sentence_pos_list.append("RB")
        RB_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "RBR":
        sentence_pos_list.append("RBR")
        RBR_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "RBS":
        sentence_pos_list.append("RBS")
        RBS_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "RP":
        sentence_pos_list.append("RP")
        RP_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "TO":
        sentence_pos_list.append("TO")
        TO_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "UH":
        sentence_pos_list.append("UH")
        UH_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VB":
        sentence_pos_list.append("VB")
        VB_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VBD":
        sentence_pos_list.append("VBD")
        VBD_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VBG":
        sentence_pos_list.append("VBG")
        VBG_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VBN":
        sentence_pos_list.append("VBN")
        VBN_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VBP":
        sentence_pos_list.append("VBP")
        VBP_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "VBZ":
        sentence_pos_list.append("VBZ")
        VBZ_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "WDT":
        sentence_pos_list.append("WDT")
        WDT_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "WP":
        sentence_pos_list.append("WP")
        WP_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "WP$":
        sentence_pos_list.append("WP$")
        WP2_list.append(pos_tagged_words[x][0])
    elif pos_tagged_words[x][1] == "WRB":
        sentence_pos_list.append("WRB")
        WRB_list.append(pos_tagged_words[x][0])
    else:
        print('Unknown Parts of Speech / symbols')

# for x in all_pos:
#     if '$' in x:
#         x = x.replace('$','2')
#         print(f'{x + _list}', end ='^^^')
#     else:
#         print(f'{x + _list}', end = '\n')

sentence_pos_list = list(dict.fromkeys(sentence_pos_list))

print(f'List of all the unique POS in the sentence is {sentence_pos_list}')

# dict(zip(sentence_pos_list, XXXXXXX ))

pos_to_relation = []

for x in sentence_pos_list:
    if '$' in x:
        x = x.replace('$','2')
        pos_to_relation.append(x + '_list')
    else:
        pos_to_relation.append(x + '_list')

print(f'POS to relation is : {pos_to_relation}')

dict_1 = {}

pos_to_relation_list = [ eval(y) for y in pos_to_relation ]

dict_sentence = dict( zip(sentence_pos_list, pos_to_relation_list))

print(f'Dictionary is {dict_sentence}')

var = random.choice(list(dict_sentence.values()))

for key, value in dict_sentence.items(): ### Part of the program where the random values of keys are generated for a sentence
    # print(key, '-', random.choice(list(value)))
    print(random.choice(list(value)), end=' ')


# def rule1():
#     print (random.choice(PRP_list) + ' ' + random.choice(VBP_list) + ' ' + random.choice(VBG_list))
#
# def rule2():
#     print(random.choice(PRP_list) + ' ' + random.choice(VBP_list) + ' ' + random.choice(NN_list))
# # var = random.choice(rules)
#
# rules = [rule1, rule2]
#
# random.choice(rules)()