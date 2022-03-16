# -*- coding: utf-8 -*-

def edge(xa,xb,G):
    '''
    helper function to add original and reverses edges in the DAG according to implication graph of the cnf

    Parameters
    ----------
    xa : int
        id of the vertice where the edge starts from
    xb : int
        id of the vertice where the edge points to
    G : Graph
         a DAG to store the vertices

    Returns
    -------
    G : Graph
        a DAG storing vertices and their edges&rvs_edges

    '''
    
    va = G.V[xa]
    vb = G.V[xb]
    nva = G.V[-xa]
    nvb = G.V[-xb]
    if xa and xb:
        G.add_edge(nva,vb)
        G.add_edge(nvb,va)
        G.add_rvs_edge(nva,vb)
        G.add_rvs_edge(nvb,va)
    elif (xa and -xb) or (-xa and xb):
        G.add_edge(nva,vb)
        G.add_edge(vb,nva)
        G.add_rvs_edge(nva,vb)
        G.add_rvs_edge(vb,nva)
    else:
        G.add_edge(nva,vb)
        G.add_edge(nvb,nva)
        G.add_rvs_edge(nva,vb)
        G.add_rvs_edge(nvb,nva)
    return G
    
    
#
def convert_graph(n,m,clauses):
    '''
    convert cnf clauses to vertices and connected edges
    
    Parameters
    ----------
    n : int
        node number 1-n
    m : int
        clause number
    clauses : 2d nested list
        2-SAT cnf clauses, example:[[1,3],[2,-3]]

    Returns
    -------
    G : Graph
        a DAG storing vertices and their edges&rvs_edges

    '''

    #init empty graph
    G = Graph()
    
    #add vertices into graph
    for i in range(1,n+1):
        #add by id
        G.add_vert(i)
        G.add_vert(-i)
   
    #add edges
    for c in clauses:
        G = edge(c[0],c[1],G)
    return G



def dfs_first(u,s):
    '''
    Perform first DFS traversal of the graph. Push node to stack before returning.

    Parameters
    ----------
    u : Vertice
        Source vert to start.
    s : Stack
        An empty stack(global var).

    Returns
    -------
    None.

    '''

    u.visited = True
    for v in u.children:
        if v.visited == False:            
            dfs_first(v,s)
    s.push(u)
            

def dfs_second(u,n,SCC):
    '''
    Second DFS on the reversed graph, order by poping nodes from the stack.

    Parameters
    ----------
    u : Vertice
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.
    SCC : Nested List
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    u.rvs_visited = True
    SCC.append(u)
    for v in u.rvs_children:
        if v.rvs_visited == False:
            dfs_second(v,n,SCC)
    SCC.append(Vertice("SEP"))
    
def kosaraju(n,m,clauses):
    '''
    Use Kosaraju's algorithm to identify each strongly connected components

    Parameters
    ----------
    n : int
        Number of literals.
    m : int
        Number of clauses.
    clauses : 2d nested list
        2-SAT cnf clauses, example:[[1,3],[2,-3]]

    Returns
    -------
    res : str
        'UNSATISFIABLE' or 'SATISFIABLE'
    unsat_index : int/None
        if UNSATISFIABLE, return the variable that caused it.
    return_solution : list/None
        if SATISFIABLE, return a possible solution.
    '''
    
    G = convert_graph(n,m,clauses)
    s = Stack()
    
    #returns
    res = None
    return_solution = None
    unsat_index = None
    
        
    #dfs_first
    for u in G.V.values():
        if u.visited == False:
            dfs_first(u,s)  
            
    #dfs_second
    SCC = []
    while not s.is_empty:
        vert = s.pop()
        if vert.rvs_visited == False:
            dfs_second(vert,n,SCC)
    #print("SCC:",[a.id for a in SCC])
    
    #separate SCC list to list
    SCC_ls = []
    SCC_ls.append([])
    state = 0
    idx = 0 
    for v in SCC:
        if v.id !="SEP":
            SCC_ls[idx].append(v)
            state = 0
        elif v.id =="SEP" and state == 0:
            state = 1
            SCC_ls.append([])
            idx += 1
    #remove empty element
    for scc in SCC_ls:
        if not scc:
            SCC_ls.remove(scc)
    
        
    
    #convert SCC to hash table
    hash_scc = np.zeros((len(SCC_ls),2*n+1))
    for i in range(len(SCC_ls)):
        for j in SCC_ls[i]:
            if j.id>0:
                hash_scc[i][j.id] = 1
            else:
                hash_scc[i][n-j.id] = 1
    #print("hash_scc",hash_scc)   
     
    #check whether complimentary pair is inside each SCC, and produce final solutn 
    for scc in hash_scc:
        for i in range(1,n+1):
            if scc[i] and scc[n+i]:
                #if both i and -i are 1
                unsat_index = i
                res = 'UNSATISFIABLE'
                return  res, unsat_index, return_solution
    res = 'SATISFIABLE'

    #return a solution
    solution = [2]*(n+1)#start from 0
    for scc in hash_scc:
        for v in SCC:
            if v.id != 'SEP':
                if v.id > 0 and solution[v.id] == 2:
                    solution[v.id] = 0
                elif v.id < 0 and solution[-v.id] == 2:
                    solution[-v.id] = 1
                
    return_solution = solution[1:]
    
    return res, unsat_index, return_solution
