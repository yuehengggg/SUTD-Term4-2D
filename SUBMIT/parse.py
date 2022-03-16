# -*- coding: utf-8 -*-

def parse(path):
    
    #convert file inp to list of strings
    data = []
    with open(path) as f:
        for line in f:
            data.append(line)

    #parsing strings
    clauses = [[]]
    highest_lit = 0
    
    for line in data:
        element = line.split()
        if len(element) != 0 and element[0] not in ("p", "c"):
            for e in element:
                lit = int(e)
                highest_lit = max(abs(lit),highest_lit) # Change the highest literal value
                if (lit == 0):
                    clauses.append(list())
                else:
                    clauses[-1].append(lit)

    # If there is '0' in the last element of the last line, we will remove the empty clause   
    if(len(clauses[-1])==0):
        clauses.pop()
    return highest_lit,len(clauses),clauses