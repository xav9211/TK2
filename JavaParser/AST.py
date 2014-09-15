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
    def __init__(self, constructorDeclarator, body, access = None):
        self.constructorDeclarator = constructorDeclarator
        self.body = body

class ConstructorDeclarator(Node):
    def __init__(self, id, parameterList = None):
        self.id = id
        self.parameterList = parameterList

class ParameterList(Node):
    def __init__(self, parameter, parameterList = None):
        self.parameter = parameter
        self.parameterList = parameterList

class Parameter(Node):
    def __init__(self, type, varid):
        self.type = type
        self.varid = varid

class FieldDclaration(Node):
    def __init__(self, types, variableDeclarator, fieldModifiers):
        self.types = types
        self.variableDeclarator = variableDeclarator
        self.fieldModifiers = fieldModifiers

class FieldModifiers(Node):
    def __init__(self, access = None, fieldModifier = None):
        self.access = access
        self.fieldModifier = fieldModifier

class FieldModifier(Node):
    def __init__(self, fieldModiferStatic = None, fieldModifierFinal = None):
        self.fieldModifierStatic = fieldModiferStatic
        self.fieldModifierFinal = fieldModifierFinal

class FieldModifierStatic(Node):
    pass

class FieldModifierFinal(Node):
    pass

class Types(Node):
    def __init__(self, access = None, id = None):
        self.access = access
        self.id = id

class VariableDeclarator(Node):
    def __init__(self, varid = None, variableDeclarator = None, types = None):
        self.varid = varid
        self.variableDeclarator = variableDeclarator
        self.types = types

class MethodDeclaration(Node):
    def __init__(self, methodHeader, body):
        self.methodHeader = methodHeader
        self.body = body

class MethodHeader(Node):
    def __init__(self, mTypes, methodDeclarator, methodModifiers = None):
        self.mTypes = mTypes
        self.methodDeclarator = methodDeclarator
        self.methodModifiers =methodModifiers

class MTypes(Node):
    def __init__(self, types = None, voids = None):
        self.types = types
        self.voids = voids

class Voids(Node):
    pass

class MethodModifiers(Node):
    def __init__(self, access = None, methodModifier = None):
        self.access = access
        self.methodModifier = methodModifier

class MethodModifier(Node):
    def __init__(self, fieldModifier = None, methodModifier = None, methodModifierAbstract = None, methodModifierSynchronized = None):
        self.fieldModifier = fieldModifier
        self.methodModifier = methodModifier
        self.methodModifierAbstract = methodModifierAbstract
        self.methodModifierSynchronized = methodModifierSynchronized

class MethodModifierAbstract(Node):
    pass

class MethodModifierSynchronized(Node):
    pass

class MethodDeclarator(Node):
    def __init__(self, varid, parameterList):
        self.varid = varid
        self.parameterList = parameterList

class InterfaceDeclaration(Node):
    def __init__(self, interfaceModifier, id, extendsInterfaces, interfaceBody):
        self.interfaceModifier =interfaceModifier
        self.id = id
        self.extendsInterfaces = extendsInterfaces
        self.interfaceBody = interfaceBody

class InterfaceModifier(Node):
    def __init__(self, access = None):
        self.access = access

class ExtendsInterfaces(Node):
    def __init__(self, id, extendsInterfaces = None):
        self.id = id
        self.extendsInterfaces = extendsInterfaces

class InterfaceBody(Node):
    def __init__(self, interfaceBodyDeclarations = None):
        self.interfaceBodyDeclarations = interfaceBodyDeclarations

class InterfaceBodyDeclarations(Node):
    def __init__(self, interfaceBodyDeclaration, interFaceBodyDeclarations = None):
        self.interfaceBodyDeclaration = interfaceBodyDeclaration
        self.interfaceBodyDeclarations = interFaceBodyDeclarations

class InterfaceBodyDeclaration(Node):
    def __init__(self, fieldModifiers, types, varid):
        self.fieldModifiers = fieldModifiers
        self.types = types
        self.varid = varid