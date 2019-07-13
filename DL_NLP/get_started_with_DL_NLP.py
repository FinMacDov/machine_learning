# load data
from nltk.tokenize import word_tokenize
filename = '/home/fin/DL/DL_NLP/example_text.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
tokens = word_tokenize(text)
print(tokens)
