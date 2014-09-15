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
        """program : typeDeclarations"""
        p[0] = AST.Program(p.lineno(1), p[1])

        
        print p[0]

    def p_typeDeclarations(self, p):
        """typeDeclarations : typeDeclaration
                            | typeDeclarations typeDeclaration"""
        if len(p) == 2:
            p[0] = AST.TypeDeclarations(p.lineno(1), p[1])
        elif len(p) > 2:
            p[0] = AST.TypeDeclarations(p.lineno(1), p[2], p[1])

    def p_typeDeclaration(self, p):
        """typeDeclaration : classDeclaration
                            | interfaceDeclaration"""
        p[0] = AST.TypeDeclaration(p.lineno(1), p[1])

    def p_classDeclaration(self, p):
        """classDeclaration : classModifier CLASS ID inherited classBody"""
        p[0] = AST.ClassDeclaration(p.lineno(1), p[1], p[3], p[4], p[5])

    def p_classModifier(self, p):
        """classModifier : ACCESS modifier
                            | modifier
                            | ACCESS
                            | """
        if len(p) == 2:
            p[0] = AST.ClassModifier(p.lineno(1), p[1])
        elif len(p) > 2:
            p[0] = AST.ClassModifier(p.lineno(1), p[1], p[2])
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
            p[0] = AST.Inherited(p.lineno(1), p[1])
        elif len(p) > 2:
            p[0] = AST.Inherited(p.lineno(1), p[1], p[2])
        else:
            p[0] = AST.Inherited()
         
        print p[0]   
        

    def p_extends(self, p):
        """extends : EXTENDS ID"""
        p[0] = AST.Extend(p.lineno(1), p[2])

    def p_implements(self, p):
        """implements : IMPLEMENTS implement """
        p[0] = AST.Implements(p.lineno(1), p[2])

    def p_implement(self, p):
        """implement : implement ',' ID
                    | ID """
        if len(p) == 2:
            p[0] = AST.Implement(p.lineno(1), p[1])
        else:
            p[0] = AST.Implement(p.lineno(1), p[3], p[1])

    def p_classBody(self, p):
        """classBody : '{' classBodyDeclarations '}'
                    | '{'   '}' """
        if len(p) > 3:
            p[0] = AST.ClassBody(p.lineno(1), p[2])
        else:
            p[0] = AST.ClassBody()

    def p_classBodyDeclarations(self, p):
        """classBodyDeclarations : classBodyDeclaration
                                | classBodyDeclarations classBodyDeclaration"""
        if len(p) == 2:
            p[0] = AST.ClassBodyDeclarations(p.lineno(1), p[1])
        else:
            p[0] = AST.ClassBodyDeclarations(p.lineno(1), p[2], p[1])

    def p_classBodyDeclaration(self, p):
        """classBodyDeclaration : classMemberDeclaration
                                | constructorDeclaration"""
        p[0] = AST.ClassBodyDeclaration(p.lineno(1), p[1])

    def p_classMemberDeclaration(self, p):
        """classMemberDeclaration : fieldDeclaration
                                | methodDeclaration"""
        p[0] = AST.ClassMemeberDeclaration(p.lineno(1), p[1])

    def p_constructorDeclaration(self, p):
        """constructorDeclaration : ACCESS constructorDeclarator BODY
                                | constructorDeclarator BODY"""
        if len(p) == 3:
            p[0] = AST.ConstructorDeclaration(p.lineno(1), p[1], p[2])
        else:
            p[0] = AST.ConstructorDeclaration(p.lineno(1), p[2], p[3], p[1])

    def p_constructorDeclarator(self, p):
        """constructorDeclarator : ID '(' parameterList ')'
                                | ID '(' ')' """
        if len(p) == 4:
            p[0] = AST.ConstructorDeclarator(p.lineno(1), p[1])
        else:
            p[0] = AST.ConstructorDeclarator(p.lineno(1), p[1], p[3])

    def p_parameterList(self, p):
        """parameterList : parameter
                        | parameterList ',' parameter"""
        if len(p) == 2:
            p[0] = AST.ParameterList(p.lineno(1), p[1])
        else:
            p[0] = AST.ParameterList(p.lineno(1), p[3], p[1])

    def p_parameter(self, p):
        """parameter : TYPE VARID"""
        p[0] = AST.Parameter(p.lineno(1), p[1], p[2])

    def p_fieldDeclaration(self, p):
        """fieldDeclaration : fieldModifiers types variableDeclarator ';'
                            | types variableDeclarator ';' """
        if len(p) == 4:
            p[0] = AST.FieldDclaration(p.lineno(1), p[1], p[2])
        else:
            p[0] = AST.FieldDclaration(p.lineno(1), p[2], p[3], p[1])

    def p_fieldsModifiers(self, p):
        """fieldModifiers : ACCESS fieldModifier
                        | ACCESS
                        | fieldModifier"""
        if len(p) == 2:
            p[0] = AST.FieldModifiers(p.lineno(1), p[1])
        else:
            p[0] = AST.FieldModifiers(p.lineno(1), p[1], p[2])

    def p_fieldModifier(self, p):
        """fieldModifier : fieldModifierStatic fieldModifierFinal
                        | fieldModifierStatic
                        | fieldModifierFinal"""
        if len(p) == 3:
            p[0] = AST.FieldModifier(p.lineno(1), p[1], p[2])
        else:
            p[0] = AST.FieldModifier(p.lineno(1), p[1])

    def p_fieldModifierStatic(self, p):
        """fieldModifierStatic : STATIC"""
        p[0] = AST.FieldModifierStatic()

    def p_fieldModifierFinal(self, p):
        """fieldModifierFinal : FINAL"""
        p[0] = AST.FieldModifierFinal()

    def p_types(self, p):
        """types : TYPE
                | ID"""
        p[0] = AST.Types(p.lineno(1), p[1])

    def p_variableDeclarator(self, p):
        """variableDeclarator : VARID
                                | variableDeclarator '[' ']'
                                | VARID '<' types '>' """
        if len(p) > 4:
            p[0] = AST.VariableDeclarator(p.lineno(1), p[1], p[3])
        else:
            p[0] = AST.VariableDeclarator(p.lineno(1), p[1])

    def p_methodDeclaration(self, p):
        """methodDeclaration : methodHeader BODY"""
        p[0] = AST.MethodDeclaration(p.lineno(1), p[1], p[2])

    def p_methodHeader(self, p):
        """methodHeader : methodModifiers mTypes methodDeclarator
                        | mTypes methodDeclarator"""
        if len(p) == 3:
            p[0] = AST.MethodHeader(p.lineno(1), p[1],p[2])
        else:
            p[0] = AST.MethodHeader(p.lineno(1), p[2], p[3], p[1])

    def p_mTypes(self, p):
        """mTypes : types
                | voids"""
        p[0] = AST.MTypes(p.lineno(1), p[1])

    def p_voids(self, p):
        """voids : VOID"""
        p[0] = AST.Voids()

    def p_methodModifiers(self, p):
        """methodModifiers : ACCESS methodModifier
                            | methodModifier"""
        if len(p) == 2:
            p[0] = AST.MethodModifiers(p.lineno(1), p[1])
        else:
            p[0] = AST.MethodModifiers(p.lineno(1), p[1], p[2])

    def p_methodModifier(self, p):
        """methodModifier : fieldModifier methodModifier
                        | methodModifierAbstract
                        | methodModifierSynchronized"""
        p[0] = AST.MethodModifier()

    def p_methodModifierAbstract(self, p):
        """methodModifierAbstract : ABSTRACT"""
        p[0] = AST.MethodModifierAbstract()

    def p_methodModifierSynchronized(self, p):
        """methodModifierSynchronized : SYNCHRONIZED"""
        p[0] = AST.MethodModifierAbstract()

    def p_methodDeclarator(self, p):
        """methodDeclarator : VARID '(' parameterList ')' """
        p[0] = AST.MethodDeclarator(p.lineno(1), p[1], p[3])

    def p_interfaceDeclaration(self, p):
        """interfaceDeclaration : interfaceModifier INTERFACE ID extendsInterfaces interfaceBody"""
        p[0] = AST.InterfaceDeclaration(p.lineno(1), p[1], p[3], p[4], p[5])

    def p_interfaceModifier(self, p):
        """interfaceModifier : ACCESS
                            | """
        if len(p) == 2:
            p[0] = AST.InterfaceModifier(p.lineno(1), p[1])
        else:
            p[0] = AST.InterfaceModifier()

    def p_extendsInterfaces(self, p):
        """extendsInterfaces : EXTENDS ID
                            | extendsInterfaces ',' ID"""
        if len(p) == 3:
            p[0] = AST.ExtendsInterfaces(p.lineno(1), p[2])
        else:
            p[0] = AST.ExtendsInterfaces(p.lineno(1), p[3], p[1])

    def p_interfaceBody(self, p):
        """interfaceBody : '{' interfaceBodyDeclarations '}' """
        if len(p) == 3:
            AST.InterfaceBody()
        else:
            AST.InterfaceBody(p.lineno(1), p[2])

    def p_interfaceBodyDeclarations(self, p):
        """interfaceBodyDeclarations : interfaceBodyDeclaration
                                    | interfaceBodyDeclarations interfaceBodyDeclaration"""
        if len(p) == 2:
            p[0] = AST.InterfaceBodyDeclarations(p.lineno(1), p[1])
        else:
            p[0] = AST.InterfaceBodyDeclarations(p.lineno(1), p[2], p[1])

    def p_interfaceBodyDeclaration(self, p):
        """interfaceBodyDeclaration : fieldModifiers types VARID ';' """
        p[0] = AST.InterfaceBodyDeclaration(p.lineno(1), p[1], p[2],p[3])