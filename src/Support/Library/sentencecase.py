'''
Sentence case utility for working with Manipulate Capitalize plugin
@author Justin Hileman <http://justinhileman.com>
'''

import re

def sentencecase(text):
    sentences = []
    for s in re.split(r'([.!?])', text):
        # find the first alpha character then capitalize the rest of the sentence.
        for offset in range(len(s)):
            if s[offset].isalpha():
                 s = s[:offset] + s[offset:].capitalize()
                 break
         
        # put lower case I in the middle of the sentence back.
        s = re.sub(r'\bi\b', 'I', s)
        sentences.append(s)
    
    return ''.join(sentences)