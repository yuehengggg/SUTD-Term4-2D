# -*- coding: utf-8 -*-


import random
import copy

import random
import copy

def random_generate():
    v=random.randint(2,500)
    c=random.randint(v//2+1,500)
    return randomgenerate(v,c)


def randomgenerate(variable,clause):
    output=[]
    output.append(variable)
    output.append(clause)
    empty=[]
    cnf=[list(empty)for i in range(0,clause)]
    inp=list(range(1,variable+1))
    indexc=list(range(0,clause))
    
    for i in inp:
        cnfindex=random.choice(indexc)
     
        sign=random.randint(1,2)
        if sign==1:
            cnf[cnfindex].append(i)
        else:
            cnf[cnfindex].append(-i)
        if len(cnf[cnfindex])==2:
            indexc.remove(cnfindex)
    for i in indexc:
        inpcopy=copy.deepcopy(inp)
        if len(cnf[i])==1:
            if cnf[i][0]>0:
                inpcopy.remove(cnf[i][0])
            else:
                inpcopy.remove(-cnf[i][0])
        for p in range(0,2-len(cnf[i])):
            r=random.randint(1,2)
            li=len(inpcopy)
            randindex=random.randint(0,li-1)
            v=inpcopy[randindex]

            if r==1:
                cnf[i].append(v)
            if r==2:
               
                cnf[i].append(-v)
            inpcopy.remove(v)

    output.append(cnf)
    return output
