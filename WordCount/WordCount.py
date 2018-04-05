#Travis Olmstead, Stephanie Colton
#310
#Dr. Keck
#WordCount
#9/6/17

import re
import io
#import matplotlib from pyplot as plt

def readFile(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read() # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w)>=3]

def counter(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w) >= 3]
    wc = {}
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

    return len(wc)


"""def longestWord(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        #words = [w.lower() for w in words if len(w+1) > len(w) ]
    w = 0
    longest = []
    for w in range(len(words)-1):#for loop cycles through array until the last index
        if len((words[w])) < len((words[w + 1])):#computes whether the length of one word is longer than the next word
            w = w + 1
            longest = words[w]#adds word to array
    return longest"""

def eightLW(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w) >= 3]
    eightLetterWords = []
    count8 = 0
    x = 0
    for x in range(len(words)):
        if (len(words[x]) == 8):#determines if the word is eaight letters
            count8 += 1#increments counter by 1 every time it catches an eight letter word
            eightLetterWords.append(words[x])#adds that word to the new list
        x = x + 1
    return count8, eightLetterWords#return list and counter

def nineLW(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w) >= 3]
    nineLetterWords = []#new array for nine letter words
    count9 = 0#new counter
    x = 0
    for x in range(len(words)):#cycles through the words list
        if (len(words[x]) == 9):#determines nine letter words
            count9 += 1#increments counter
            nineLetterWords.append(words[x])#adds nine letter word to new list
        x = x + 1
    return count9, nineLetterWords#returns new list and counter

def tenLW(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w) >= 3]
    tenLetterWords = []#new list for ten letter words
    count10 = 0#new counter
    for x in range(len(words)):#cycles through list
        if (len(words[x]) == 10):#finds ten letter words
            count10 += 1#increment counter when ten letter word is found
            tenLetterWords.append(words[x])#adds word to list
        x = x + 1#next element in words list
    return tenLetterWords, count10#returns new list and counter

def elevenLW(textFile):
    pattern = re.compile(r'\w+')
    with io.open(textFile) as f:
        text = f.read()  # read as a single large string
        words = pattern.findall(text)  # pull out words
        words = [w.lower() for w in words if len(w) >= 3]
    elevenLetterWords = []#new array for eleven letter words
    count11 = 0#new counter
    x = 0
    for x in range(len(words)):#cycles through words list
        if (len(words[x]) == 11):#if word is eleven letters
            count11 += 1#increment counter
            elevenLetterWords.append(words[x])#add word to new list
        x = x + 1
    return count11, elevenLetterWords#returns new list and counter

#PyPlot Stuff:

# men_means = (20, 35, 30, 35)
"""words1Vals = [eightLW('wordCount2.txt')[0], nineLW('wordCount2.txt')[1], tenLW('wordCount2.txt')[2], elevenLW('wordCount2.txt')]
words2Vals = [eightLW('Swannsway.txt')[0], nineLW('Swannsway.txt')[1], tenLW('Swannsway.txt')[2], elevenLW('Swannsway.txt')]
N = len(words1Vals)
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
print('')
print('')
print(words1Vals)
fig, ax = plt.subplots()
rects1 = ax.bar(ind, words1Vals, width, color='r')

# women_means = (25, 32, 34, 20)
rects2 = ax.bar(ind + width, words2Vals, width, color='y')

# add some text for labels, title and axes ticks
ax.set_xlabel('Word Length')
ax.set_ylabel('Word Count')
ax.set_title('Word Lengths')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('8','9','10','11'))


ax.legend((rects1[0], rects2[0]), ('File1', 'File2'))


def autolabel(rects):

    #Attach a text label above each bar displaying its height

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()"""


print(counter('wordCount2.txt'))
print(counter('swannsway.txt'))
#print(longestWord('wordCount2.txt'))
print(eightLW('wordCount2.txt'))
print()
print(nineLW('wordCount2.txt'))
print()
print(tenLW('wordCount2.txt'))
print()
print(elevenLW('wordCount2.txt'))
print()
print((eightLW('swannsway.txt')))
print()
print(nineLW('swannsway.txt'))
print()
print(tenLW('swannsway.txt'))
print()
print(elevenLW('swannsway.txt'))

plt.xlabel("Word Length")
plt.ylabel("Number of words")
plt.plot(list((eightLW("swannsway.txt")[0]),list((eightLW("wordCount2.txt")[1]))))
plt.plot(list(wlen2.keys()), list(wlen2.values()), 'bo')
plt.show()
