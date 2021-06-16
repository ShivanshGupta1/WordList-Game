#!/usr/bin/env python
# coding: utf-8

# In[3]:


myWords = [eachWord.strip() for eachWord in open("wordlist.txt","r")]
threeLetterWords = []
for word in myWords:
    if len(word)==3:
        threeLetterWords.append(word)
print(threeLetterWords)


# In[17]:


myNewWords = [eachWord.strip() for eachWord in open("wordlist.txt","r")]
wordsWithConditions = []
for words in myNewWords:
    checkWord = words[:2]
    if checkWord=="kn" or checkWord=="gn":
        wordsWithConditions.append(words)
print(wordsWithConditions)


# In[4]:


myNewWords = [eachWord.strip() for eachWord in open("wordlist.txt","r")]
wordsWithVowles = []
for words in myNewWords:
    if "a" in words or "e" in words or "i" in words or "o" in words or "u" in words:
        wordsWithVowles.append(words)
percentgage = (len(wordsWithVowles)/len(myNewWords))*100
print(percentgage)
print(wordsWithVowles)

