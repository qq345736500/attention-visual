import random
sent = '''I LOVE YOU'''
words = sent.split()
word_num = len(words)
attention = [(x+1.)/word_num*100 for x in range(word_num)]
import random
random.seed(43)
random.shuffle(attention)
color = 'red'
# generate(words, attention, "sample.tex", color)



print(words)

