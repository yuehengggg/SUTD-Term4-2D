# -*- coding: utf-8 -*-

class Stack:
    def __init__(self):
        self.__items = []
        
    def peek(self):
        if self.__items:
            return self.__items[-1]
        
    def pop(self):
        if not self.is_empty:
            return self.__items.pop()
        
    def push(self,val):
        self.__items.append(val)
    
    @property
    def is_empty(self):
        return len(self.__items) == 0
    
    @property
    def size(self):
        return len(self.__items)
 
        
class Vertice:
    def __init__(self,id=None):
        self.id = id
        self.solu = None
        self.visited = False
        self.rvs_visited = False
        self.children = []
        self.rvs_children = []
        
    def add_edge(self,v):
        if v not in self.children:
            self.children.append(v)
    
    def add_rvs_edge(self,v):
        if v not in self.rvs_children:
            self.rvs_children.append(v)
               
class Graph:
    def __init__(self):
        self.V = {} #vertices, [id]=Vertice
         
    def add_vert(self,id):
        self.V[id] = Vertice(id)
    
    def remove_vert(self,id):
        del self.V[id] 
    
    def add_edge(self,vfrom,vto):
        vfrom.add_edge(vto)
        
    def add_rvs_edge(self,vfrom,vto):
        vto.add_rvs_edge(vfrom) 