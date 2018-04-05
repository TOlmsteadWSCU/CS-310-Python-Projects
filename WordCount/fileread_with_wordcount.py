import re   # regular expressions
import io


word_pattern = re.compile(r'\w+')
# with version ensures closing even if there are failures
with io.open("swannsway.txt") as f:
    text = f.read() # read as a single large string
    words = word_pattern.findall(text)  # pull out words
    words = [w.lower() for w in words if len(w)>=3]

print(len(words))

#%timeit  'boojum' in words


wc = {}
for word in words:
    if word in wc:
        wc[word]+=1
    else:
        wc[word]=1

len(wc)
print(wc)

#%timeit 'boojum' in wc

max(wc.values())

sorted(wc.items(), key = lambda x:x[1], reverse=True)[:100]
sorted(wc.items(), key = lambda x:x[1], reverse=True)[-100:]


import collections

wc = collections.Counter(words)
sorted(wc.items(), key = lambda x:x[1], reverse=True)[:100]

# how many words of different lengths?

wlen = collections.Counter([len(word) for word in words])

wlen


#from matplotlib import pyplot as plt
#%matplotlib inline
#plt.plot(list(wlen.keys()),list(wlen.values()),'bo')
