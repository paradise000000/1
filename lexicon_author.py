import string
import pymorphy2
from collections import Counter
 
Voinaimir_T1 = open('voyna-i-mir-tom-1.txt')
VIM1=Voinaimir_T1.read()
 
text = [word.strip(string.punctuation) for word in VIM1.split()]
text2 = [morph.parse(word)[0].normal_form for word in text]
text3=Counter(text2)
len(text3)
 
out: 10819
