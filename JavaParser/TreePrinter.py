import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self):
        result = ""
        return result


    @addToClass(AST.Program)
    def printTree(self):
        result = ""
        # dokonczyc