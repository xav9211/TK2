#!/usr/bin/python

class Node(object):

    def __str__(self):  
        return self.printTree(0)
    
    
    

class Program(Node):
    def __init__(self, access, type, id, inherited, body):
        self.access = access
        self.type = type
        self.id = id
        self.inherited = inherited
        self.body = body
        


class Inherited(Node):
    def __init__(self,extend = None,implements = None):
        self.extend = extend
        self.implements = implements
        
class Extend (Node):
    def  __init__(self, id):
        self.id  = id
        
class Implements (Node):
    def __init__(self,implement):
        self.implement = implement


class Implement (Node):
    def __init__(self,id,implement = None):
        self.id = id
        self.implement = implement