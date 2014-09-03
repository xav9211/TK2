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

#dokonczyc