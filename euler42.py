''' Euler 42 '''
import math
import numpy as np

'''
Needs words_42.txt to work

I loop over every character in the text file. When I hit a letter, I start
adding value.  When I hit a non-letter like a quotation mark, I stop counting
and check if the word value is a triangle number.
'''

def is_tri(x):
    tn = (math.sqrt(8*x+1)-1)/2
    if tn%1 == 0:
        return True
    else:
        return False

words = np.loadtxt('words_42.txt',dtype=str)#,unpack=True)
words = str(words)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def number_val(x):
    x=str(x)
    for i in range(len(alphabet)):
        if alphabet[i] == x:
            return i+1

triwords = 0
count = 0 # acts like an on/off switch for counting up value and checking value
val = 0
for i in words:

    if i in alphabet:
        count = 1
    else:
        count = 0
    if count == 1:
        val += number_val(i)
    if count == 0:
        if is_tri(val) and val != 0:
            triwords += 1
        val = 0

print(triwords)
