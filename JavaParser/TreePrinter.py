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
        result += self.access
        result += self.type
        result += self.id
        result += self.inherited.printTree(indent)
        result += self.body
        
        
        
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
