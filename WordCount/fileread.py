import re   # regular expressions
import io


word_pattern = re.compile(r'\w+')
# with version ensures closing even if there are failures
with io.open("swannsway.txt") as f:
    text = f.read() # read as a single large string
    words = word_pattern.findall(text)  # pull out words
    words = [w.lower() for w in words if len(w)>=3]

print(len(words))
