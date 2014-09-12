#!/usr/bin/python

class Node(object):

    def __str__(self):  
        return self.printTree(0)
    
    
    

class Program(Node):
    def __init__(self, typeDeclatations = None):
        self.typeDeclarations = typeDeclatations

class TypeDeclarations(Node):
    def __init__(self, typeDeclaration, typeDeclarations = None):
        self.typeDeclaration = typeDeclaration
        self.typeDeclarations = typeDeclarations

class TypeDeclaration(Node):
    def __init__(self, classDeclaration = None, interfaceDeclaration = None):
        self.classDeclaration = classDeclaration
        self.interfaceDeclararion = interfaceDeclaration

class ClassDeclaration(Node):
    def __init__(self, classModifier, id, inherited, classBody):
        self.classModifier = classModifier
        self.id = id
        self.inherited = inherited
        self.classBody = classBody

class ClassModifier(Node):
    def __init__(self, access = None, modifier = None):
        self.access = access
        self.modifier = modifier

class Modifier(Node):
    pass

class Inherited(Node):
    def __init__(self, extend = None,implements = None):
        self.extend = extend
        self.implements = implements
        
class Extend(Node):
    def  __init__(self, id):
        self.id  = id
        
class Implements(Node):
    def __init__(self, implement):
        self.implement = implement


class Implement(Node):
    def __init__(self, id, implement = None):
        self.id = id
        self.implement = implement

class ClassBody(Node):
    def __init__(self, classBodyDeclarations = None):
        self.classBodyDeclarations = classBodyDeclarations

class ClassBodyDeclarations(Node):
    def __init__(self, classBodyDeclaration, classBodyDeclarations = None):
        self.classBodyDeclaration = classBodyDeclaration
        self.classBodyDeclarations = classBodyDeclarations

class ClassBodyDeclaration(Node):
    def __init__(self, classMemberDeclaration = None, constructorDeclaration = None):
        self.classMemberDeclaration = classMemberDeclaration
        self.constructorDeclaration = constructorDeclaration

class ClassMemeberDeclaration(Node):
    def __init__(self, fieldDeclaration = None, methodDeclaration = None):
        self.fieldDeclaration = fieldDeclaration
        self.methodDeclaration = methodDeclaration

class ConstructorDeclaration(Node):
    def __init__(self, constructorDeclarator, constructorBody, access = None):
        self.constructorDeclarator = constructorDeclarator
        self.constructorBody = constructorBody



class InterfaceDeclaration(Node):
    def __init__(self, interfaceModifier, id, extendsInterfaces, body):
        self.interfaceModifier =interfaceModifier
        self.id = id
        self.extendsInterfaces = extendsInterfaces
        self.body = body

class InterfaceModifier(Node):
    def __init__(self, access = None):
        self.access = access

class ExtendsInterfaces(Node):
    def __init__(self, id, extendsInterfaces = None):
        self.id = id
        self.extendsInterfaces = extendsInterfaces