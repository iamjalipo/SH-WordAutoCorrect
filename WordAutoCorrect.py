import re
from collections import Counter
import numpy as np
import pandas as pd



def delete_letter(word):
    s1 = []
    for i in range(len(word)):
        h1 = word
        if i == 0:
            h1 = h1[i+1:]
            s1.append(h1)
        elif i == len(word)-1:
            h1 = h1[:-1]
            s1.append(h1)
        else:
            h1  = h1[:i] + h1[i+1:]
            s1.append(h1)
    return (set(s1))    

def replace_letter(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s2 = []
    for i in range(len(word)):
        for j in range(len(alpha)):
            h = word
            if i == 0 :
                h = alpha[j] + h[1:] 
                s2.append(h)
            elif i== len(word)-1:
                h = h[:-1] + alpha[j]
                s2.append(h)
            else:
                h = h[:i] + alpha[j] + h[i+1:]
                s2.append(h)
    return (set(s2))
    
def insert_letter(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s3 = []
    for i in range(len(word)+1):
        for j in range(len(alpha)):
            h = word
            if i == 0 :
                h = alpha[j] + h 
                s3.append(h)
            else:
                h = h[:i] + alpha[j] + h[i:]
                s3.append(h)            
    return (set(s3))


def edit_one_letter(word):
    
    edit_one_set = set()
    edit_one_set.update(delete_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    
    res = dict()
    res1 = dict.fromkeys(delete_letter(word), 1) 
    res2 = dict.fromkeys(replace_letter(word), 2) 
    res3 = dict.fromkeys(insert_letter(word), 1) 
    
    res.update(res1)
    res.update(res2)
    res.update(res3)
    
    return edit_one_set , res 

def edit_two_letter(word , grade):
    edit_two_set = set()
    edit_two_set.update(delete_letter(word))
    edit_two_set.update(replace_letter(word))
    edit_two_set.update(insert_letter(word))
    
    res = dict()
    res1 = dict.fromkeys(delete_letter(word), grade+1) 
    res2 = dict.fromkeys(replace_letter(word), grade+2) 
    res3 = dict.fromkeys(insert_letter(word), grade+1) 
    
    res.update(res1)
    res.update(res2)
    res.update(res3)
    
    return edit_two_set , res


def clean(text):
    cleantext = []
    for txt in text:
        if txt == ' ':
            pass
        else:
            txt = ''.join([i for i in txt if not i.isdigit()])
            txt = txt.replace(',' , '')
            txt = txt.replace(')' , '')
            txt = txt.replace('(' , '')
            txt = txt.replace(';' , '')
            txt = txt.replace(':' , '')
            txt = txt.replace('.' , '')
            txt = txt.replace('?' , '')
            txt = txt.replace('!' , '')
            txt = txt.replace('[' , '')
            txt = txt.replace(']' , '')
            txt = txt.replace('<' , '')
            txt = txt.replace("'" , '')
            if len(txt) != 0:
                if txt[0] == "-" or txt[-1] == "-":
                    txt = txt.replace("-" , '')
            cleantext.append(txt) 
            
    return cleantext

def unigram(montakhab , cleantext):
    CT = set(cleantext)
    ehtemal = dict()
    for i in montakhab:
        count = 0
        for j in cleantext:
            if i == j:
                count += 1
        
        ehtemal[i] = count/len(CT)

    return ehtemal 

def autoCorrect(word):

    x = []
    with open("shakespeare.txt") as data:
        text = re.sub(r'\s+', ' ', data.read())
        text = text.split(' ')
        for i in text:
                x.append(i.lower())

    cleantext = clean(x)


    word = word.lower()
    semiset , semidict = edit_one_letter(word)
    final_set = set()
    final_dict = dict()
    for i in list(semiset):
        l , k = edit_two_letter(i , semidict[i])
        final_set.update(l)
        final_dict.update(k)

    final_set.update(semiset)
    final_dict.update(semidict)

    total = final_set & set(cleantext)
    
    grade = dict()
    for i in total:
        grade[i] = final_dict[i] 

    key_min = min(grade.keys(), key=(lambda k: grade[k]))
    star = grade[key_min]
    montakhab = []
    if len(montakhab) == 1:
        result = montakhab[0]
    else : 
        for i in total:
            if grade[i] == star:
                montakhab.append(i)

        ehtemal = unigram(montakhab , cleantext)  
        key_max = max(ehtemal.keys(), key=(lambda k: ehtemal[k]))
        result = key_max      

    return result
	
	
if __name__ == "__main__":
    
	WORD = str(input('Enter a word:- '))
		
	print(autoCorrect(WORD))