#!/usr/bin/env python
#https://stackoverflow.com/questions/2635453/how-to-include-clean-target-in-makefile

from __future__ import print_function

import sys
import string
import hashlib
import pickle

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n"): return x[:-1]
    if x.endswith("\r"): return x[:-1]
    return x

def get_var_name(**kwargs): return kwargs.keys()[0]
# https://stackoverflow.com/questions/2553354/how-to-get-a-variable-name-as-a-string
def update_dict(inDict, inElement):
    if inElement in inDict:
        inDict[inElement] = inDict[inElement] + 1
    else:
        inDict[inElement] = 1

def pickle_dict(inDict, dictName):
    '''Pickle a Dictionary.
    
    Keyword arguments:
    inDict -- input dictionary
    dictName -- name of the dictionary 
    '''
    with open('%s.pickle' %dictName, 'wb') as handle:
        pickle.dump(inDict, handle, protocol=pickle.HIGHEST_PROTOCOL) 

def unpickle_dict(dictToRetrieve = "inDict.pickle"):
    with open(dictToRetrieve, 'rb') as handle:
        return pickle.load(handle)  

###
dictSingle = unpickle_dict("dictSingles.pickle")
dictDuos = unpickle_dict("dictDuos.pickle")
dictTrios = unpickle_dict("dictTrios.pickle")
First = False
Second = False
        
args = str(sys.argv[1:])

for words in args:
    words = words.replace('\\r"]',"")
    words = words.replace('\\r\\n'," ")
    words = words.replace('\\r', "")
    
str1 = args
str2 = str1.translate(None, ".").lower()
str1 = str2.translate(None, ",")
str2 = str1.translate(None, "?")
wrappers = [":","(",")","[","]","\""]

str2 = str2.split(" ")

for items in str2:
    items = items.replace("]","")
    items = items.replace("\\r","")
    items = items.replace("(","")
    items = items.replace(")","")
    items = items.replace("\\","")
    items = items.replace("[","")
    items = items.replace(";","")  
    items = items[1:-1]
    items = items.replace('"','')  
    #print(hashlib.sha1(items).hexdigest() )
    # main event
    if not First:
        First = True
        prev2 = items
        update_dict(dictSingle,items)
    else:
        if not Second:
            Second = True
            prev = items
            update_dict(dictSingle,items)
            update_dict(dictDuos,prev2+"_"+prev)
        else:
            #prev = this
            #prev2 = prev
            this = items
            #prev
            #prev2
            update_dict(dictSingle,items)
            update_dict(dictDuos,prev2+"_"+prev)
            update_dict(dictTrios,prev2+"_"+prev+"_"+this)
            prev2 = prev
            prev = this


pickle_dict(dictSingle,"dictSingles")
pickle_dict(dictDuos,"dictDuos")
pickle_dict(dictTrios,"dictTrios")           

dTout = sorted(dictSingle.iteritems(), key=lambda (k,v): (v,k) )

print(dTout)
print(len(dTout))            
#print(dTout)
    
