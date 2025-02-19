#Program to generate regular expression for a given grammer

import re
grammer ={"S":['A','AB'],"A":['aB'], "B": ['b']}

def generate_rejax(non_terminals):
    rejax=" "
    for production in grammer[non_terminals]:
        r= " "
        for symbol in production:
            if symbol.isupper():
                r=r+generate_rejax(symbol)
            else:
                r=r+symbol
        rejax=rejax + r + '/'
    return rejax[::-1]
#main
S=generate_rejax('S')
print("Expression",S)
