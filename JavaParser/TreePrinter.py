import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

def addIndent(indent):
    result = ""
    i = 0
    while i < indent:
        result += " "
        i += 1
    return result

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

   
    
    @addToClass(AST.Program)
    def printTree(self, indent):
        result = ""
        result = addIndent(indent)
        return result
        
        
        
        return result

    @addToClass(AST.TypeDeclarations)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.TypeDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassModifier)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.Modifier)
    def printTree(self, indent):
        result = addIndent(indent)
        return result
    
    @addToClass(AST.Inherited)
    def printTree(self, indent):
        result = addIndent(indent)
        return result
    
    
    @addToClass(AST.Implement)
    def printTree(self, indent):
        result = addIndent(indent)
        return result
    
    @addToClass(AST.Implements)
    def printTree(self, indent):
        result = addIndent(indent)
        return result
    
    @addToClass(AST.Extend)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassBody)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassBodyDeclarations)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassBodyDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ClassMemeberDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ConstructorDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ConstructorDeclarator)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ParameterList)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.Parameter)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.FieldDclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.FieldModifiers)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.FieldModifier)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.FieldModifierStatic)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.FieldModifierFinal)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.Types)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.VariableDeclarator)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MethodDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MethodHeader)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MTypes)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.Voids)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MethodModifiers)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MethodModifier)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.MethodDeclarator)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.InterfaceDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.InterfaceModifier)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.ExtendsInterfaces)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.InterfaceBody)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.InterfaceBodyDeclarations)
    def printTree(self, indent):
        result = addIndent(indent)
        return result

    @addToClass(AST.InterfaceBodyDeclaration)
    def printTree(self, indent):
        result = addIndent(indent)
        return result