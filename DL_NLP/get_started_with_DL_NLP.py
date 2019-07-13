# load data
from nltk.tokenize import word_tokenize

# Code options
write_output = False

# filename = '/home/fin/DL/DL_NLP/example_text.txt'
filename = '/home/fin/DL/DL_NLP/tale_of_two_cities.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# split into words
tokens = word_tokenize(text)

# Write new output
fname = 'token_output.txt'

if write_output is True:
    with open(fname, 'w+') as f:
        for item in tokens:
            f.write("%s\n" % item)
