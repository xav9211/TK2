#!/usr/bin/python

from scanner import Scanner
import AST

class Cparser(object):


    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()

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

    def p_inherited(self, p):
        """inherited : extend implements
                    | implements extend
                    | extend
                    | implements
                    | """

    def p_extend(self, p):
        """extend : EXTENDS ID"""

    def p_implements(self, p):
        """implements : implements implement
                    | """

    def implement(self, p):
        """implement : IMPLEMENTS ID"""