# -*- coding: utf-8 -*-


import random
import copy

def random_generate():
    '''
    Randomly generate test cases

    '''
    v=random.randint(1,500)
    c=random.randint(1,500)
    return randomgenerate(v,c)


def randomgenerate(variable,clause):
    output=[]
    output.append(variable)
    output.append(clause)
    cnf=[]
    inp=list(range(1,variable+1))
    for i in range(0,clause):
        c=[]
        inpcopy=copy.deepcopy(inp)
        for p in range(0,2):
            r=random.randint(1,2)
            l=len(inpcopy)
            randindex=random.randint(0,l-1)
            v=inpcopy[randindex]
            if r==1:
                c.append(v)
            if r==2:
               
                c.append(-v)
            inpcopy.remove(v)        
        cnf.append(c)
    output.append(cnf)
    return output