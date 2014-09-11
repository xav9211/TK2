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
        """program : ACCESS TYPE ID inherited BODY"""
        p[0] = AST.Program( p[1],p[2],p[3],p[4], p[5])
        
        print p[0]
        

    def p_inherited(self, p):
        """inherited : extends implements
                    | extends
                    | implements
                    | """
        if len(p)==2 :
            p[0] = AST.Inherited(p[1])
        
        elif len(p)> 2:
            p[0] = AST.Inherited(p[1],p[2])
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
        if len(p)==2:
            p[0] = AST.Implement(p[1])
        else:
            p[0] = AST.Implement(p[3], p[1])