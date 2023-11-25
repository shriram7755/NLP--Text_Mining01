# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:26:42 2023

@author: SHRI
"""
################## Text Mining #####################################
sentence ="we are Learning TextMining from Sanjivani AI"
#if you want to know the position of learning
sentence.index("Learning")
#This is showing the charactor index from o in including


###########################################################
#we want to know the position TextMining word
sentence.split().index("TextMining")
#it will split of words in a list and count the position
#if you want to see the list selected sentence.split() and
#it will show at 3

####################################################################
#Suppose we want print any word in Reverse Order
sentence.split()[2][::-1]
###[start:end end:-1(start)] will start from -1,-2,-3  till the end
### learning will  be printed as gninrael



#suppose want to print first and last word of the sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word


#now we concat the first and last word
concat_word = first_word +"  "+last_word
concat_word


######################################################################
#we want to print the even word from the sentences
[words[i] for i in range(len(words)) if i%2==0]
#words having odd length will not be printed 

##################################################################
sentence
#now we want to display only AI
sentence[-3:]
## it will start from -3,-2 -1 i.e AI

#####################################################################
#Suppose we want to select each word and print in reversed order
sentence[::-1]
#'IA inavijnaS morf gniniMtxeT gninraeL era ew'

###################################################################
#Suppose we want to select each word and print in reversed order
words
print(" ".join(word[::-1] for word in words))
#ew era gninraeL gniniMtxeT morf inavijnaS IA


#--------------------------- Tokenization ---------------------------------------------------
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)

#---------------------------------------------------------------------------------
#parts of speech tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#it is going mention parts of speech

#--------------------------------------------------------------------------------
#stop word from nltk library
import nltk
nltk.download('stopwords')


from nltk.corpus import stopwords
stop_words=stopwords.words('English')
##you can verify 179 stop words in variable explore
print(stop_words)
sentence1="I am Learning NLP:It is one of the most popular library in python"
#first we will tokenize the sentence
sentence_words=word_tokenize(sentence1)
print(sentence_words)


## Now lets us filter the sentence using stop_words
sentence_no_stops=" ".join([words for words in sentence_words if words not in stop_words])
print(sentence_no_stops)
sentence1

# now we can notice that am ,is, of , the most,popular , in are missing 
#-------------------------------------------------------------------------------
#Suppose we want to replace words in string
sentence2 = "I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India").replace("-19","-2020")
print(normalized_sentence)


#------------------------------------------------------------------------
#suppose want to auto correction in the sentence
from autocorrect import Speller
#Declare the function Speller defined from English
spell=Speller(lang='en')
spell("brth")

#Suppose we want to correct whole sentence 
sentence3="Ntiral Lamguge proccing deals withn the aart of extractig setiiments"
##let us first tokenise these sentence
sentence3=word_tokenize(sentence3)
#sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)

#-----------------------------------------------------------------------------------------------
#Stemmming 
stemmer=nltk.stem.PorterStemmer()
stemmer.stem('programming')
stemmer.stem('programmed')
stemmer.stem('Jumping')
stemmer.stem('Jumped')

#--------------------------------------------------------------------------------------------

#Leamatizer
#Lematizer looks into  dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")

lemmatizer.lemmatize("battling")

lemmatizer.lemmatize("amazing")

#--------------------------------------------------------------------------------------------
## chunking  (Shallow Parsing ) Identifying namned entities
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="We are Learning NLP in python by SanjivaniAI "
##first we will tokenize
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

#--------------------------------------------------------------------------------------------
#Semntence Tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we re NLP in Python.Delivered by SanjivaniAI. Do you know where it is located? It is in Kopargaon")
sent
#--------------------------------------------------------------------------------------------

from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))

sentence2="it is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))


#Synset('bank.v.07') a slope in the turn of a road or truck;
# the outside is higher than the inside in order to reduce the 
###
#'bank' as multiple meanings. if you want to find exact meaning
#execute the following code
#The defination of bank can be seen here

from nltk.corpus import wordnet as wn
for ss in wn.synsets('bank'): print(ss.definition())
#--------------------------------------------------------------------------------------------