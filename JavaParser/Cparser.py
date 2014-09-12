#!/usr/bin/python

from scanner import Scanner
import AST
import TreePrinter

class Cparser(object):


    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()
        self.tree = None

    tokens = Scanner.tokens

    # precedence = (
    #    ("nonassoc", 'IFX'),
    #    ("nonassoc", 'ELSE'),
    #    ("right", '='),
    #    ("left", 'OR'),
    #    ("left", 'AND'),
    #    ("left", '|'),
    #    ("left", '^'),
    #    ("left", '&'),
    #    ("nonassoc", '<', '>', 'EQ', 'NEQ', 'LE', 'GE'),
    #    ("left", 'SHL', 'SHR'),
    #    ("left", '+', '-'),
    #    ("left", '*', '/', '%'),
    # )

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, self.scanner.find_tok_column(p), p.type, p.value))
        else:
            print('At end of input')

    def p_program(self, p):
        """program : typeDeclarations
                    | """
        if len(p) == 2:
            p[0] = AST.Program(p[1])
        else:
            p[0] = AST.Program()
        
        print p[0]

    def p_typeDeclarations(self, p):
        """typeDeclarations : typeDeclaration
                            | typeDeclarations typeDeclaration"""
        if len(p) == 2:
            p[0] = AST.TypeDeclarations(p[1])
        elif len(p) > 2:
            p[0] = AST.TypeDeclarations(p[2], p[1])

    def p_typeDeclaration(self, p):
        """typeDeclaration : classDeclaration
                            | interfaceDeclaration
                            | """
        if len(p) == 2:
            p[0] = AST.TypeDeclaration(p[1])
        else:
            p[0] = AST.TypeDeclaration()

    def p_classDeclaration(self, p):
        """classDeclaration : classModifier CLASS ID inherited classBody"""
        p[0] = AST.ClassDeclaration(p[1], p[3], p[4], p[5])

    def p_classModifier(self, p):
        """classModifier : ACCESS modifier
                            | modifier
                            | ACCESS
                            | """
        if len(p) == 2:
            p[0] = AST.ClassModifier(p[1])
        elif len(p) > 2:
            p[0] = AST.ClassModifier(p[1], p[2])
        else:
            p[0] = AST.ClassModifier()

    def p_modifier(self, p):
        """modifier : ABSTRACT
                    | FINAL"""
        p[0] = AST.Modifier()

    def p_inherited(self, p):
        """inherited : extends implements
                    | extends
                    | implements
                    | """
        if len(p) == 2:
            p[0] = AST.Inherited(p[1])
        
        elif len(p) > 2:
            p[0] = AST.Inherited(p[1], p[2])
        else:
            p[0] = AST.Inherited()
         
        print p[0]   
        

    def p_extends(self, p):
        """extends : EXTENDS ID"""
        p[0] = AST.Extend(p[2])

    def p_implements(self, p):
        """implements : IMPLEMENTS implement """
        p[0] = AST.Implements(p[2])

    def p_implement(self, p):
        """implement : implement ',' ID
                    | ID """
        if len(p) == 2:
            p[0] = AST.Implement(p[1])
        else:
            p[0] = AST.Implement(p[3], p[1])

    def p_classBody(self, p):
        """classBody : '{' classBodyDeclarations '}'
                    | '{'   '}' """
        if len(p) > 3:
            p[0] = AST.ClassBody(p[2])
        else:
            p[0] = AST.ClassBody()

    def p_classBodyDeclarations(self, p):
        """classBodyDeclarations : classBodyDeclaration
                                | classBodyDeclarations classBodyDeclaration"""
        if len(p) == 2:
            p[0] = AST.ClassBodyDeclarations(p[1])
        else:
            p[0] = AST.ClassBodyDeclarations(p[2], p[1])

    def p_classBodyDeclaration(self, p):
        """classBodyDeclaration : classMemberDeclaration
                                | constructorDeclaration"""
        p[0] = AST.ClassBodyDeclaration(p[1])

    def p_classMemberDeclaration(self, p):
        """classMemberDeclaration : fieldDeclaration
                                | methodDeclaration"""
        p[0] = AST.ClassMemeberDeclaration(p[1])

    def p_constructorDeclaration(self, p):
        """constructorDeclaration : ACCESS constructorDeclarator constructorBody
                                | constructorDeclarator constructorBody"""
        if len(p) == 3:
            p[0] = AST.ConstructorDeclaration(p[1], p[2])
        else:
            p[0] = AST.ConstructorDeclaration(p[2], p[3], p[1])



    def p_interfaceDeclaration(self, p):
        """interfaceDeclaration : interfaceModifier INTERFACE ID extendsInterfaces BODY"""
        p[0] = AST.InterfaceDeclaration(p[1], p[3], p[4], p[5])

    def p_interfaceModifier(self, p):
        """interfaceModifier : ACCESS
                            | """
        if len(p) == 2:
            p[0] = AST.InterfaceModifier(p[1])
        else:
            p[0] = AST.InterfaceModifier()

    def p_extendsInterfaces(self, p):
        """extendsInterfaces : EXTENDS ID
                            | extendsInterfaces ',' ID"""
        if len(p) == 3:
            p[0] = AST.ExtendsInterfaces(p[2])
        else:
            p[0] = AST.ExtendsInterfaces(p[3], p[1])