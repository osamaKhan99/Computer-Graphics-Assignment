from nltk.corpus import inaugural
from nltk import FreqDist
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
print("All fields of inaugural corpus ", inaugural.fileids())

totalNumOfWords = len(inaugural.words('1993-Clinton.txt'))
print("Total number of words in 1993-Clinton's Speech = ", totalNumOfWords);

print("Total Distinct Words = ", len(set(inaugural.words('1993-Clinton.txt'))))

count = 0
for i in inaugural.words('1993-Clinton.txt'):
    count = count + len(i)
print("Average Length of Words = ", round(count / totalNumOfWords))

########################################

print(inaugural.words('1993-Clinton.txt'))

allWords = inaugural.words('1993-Clinton.txt')
lowerCase = [i for i in allWords if i.islower()]
freqDist = FreqDist(lowerCase)
print(freqDist)
print(freqDist.most_common(10))

stopWords = stopwords.words("english")
notStopWords = [i for i in allWords if i not in stopWords]
freqDist02 = FreqDist(notStopWords)
print(freqDist02.most_common(10))


plotWords = FreqDist(allWords)
plotWords.plot(10)

print("World " + str(freqDist02.pop("world")))
print("america " + str(freqDist02.pop("America")))
