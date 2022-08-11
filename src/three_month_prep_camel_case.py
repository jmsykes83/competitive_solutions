'''
Refer to the camel-case.md file for the description
of this project.
'''

import string
import re

def split(strg: string):
    '''splits the string'''
    return ' '.join(re.findall('[A-Za-z][^A-Z]*', strg))

def combine(strg:string)->string:
    '''combines the string together'''
    return ''.join(strg.split(' '))

def str_type(typ:string,first:string, strg:string) ->string:
    '''returns the string in a formated type'''
    if typ == 'V':
        return strg[:strg.find(' ')] + strg[strg.find(' '):].title() if first == 'C' else strg.lower()
    if typ == 'M':
        return strg[:strg.find(' ')] + strg[strg.find(' '):].title() + '()' if first != 'S' else strg.lower()
    if typ == 'C':
        return strg.title() if first != "S" else strg.lower()
    return 'Failed'

def set_string(strg:string)->string:
    '''Sets the string to be evaluated'''
    first,second,strin = strg.split(';')
    temp_str = re.sub("[^a-zA-Z]",'',strg[4:])
    if first == 'S':
        temp_str = split(temp_str)
        return str_type(second,first,temp_str)
    if first =='C':
        temp_str = str_type(second,first, strin)
        return combine(temp_str)
    return 'Failed'

if __name__ == "__main__":
    print(set_string(input()))