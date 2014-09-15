import ply.lex as lex


class Scanner(object):


    def find_tok_column(self, token):
        last_cr = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        if last_cr < 0:
            last_cr = 0
        return token.lexpos - last_cr


    def build(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()



    literals = "{}()<>=;:,+-*/%&|^"


    reserved = {
    'class'     : 'CLASS',
    'interface' : 'INTERFACE',
    'implements' : 'IMPLEMENTS',
    'extends'   : 'EXTENDS',
    'abstract'  : 'ABSTRACT',
    'final'     : 'FINAL',
    'static'    : 'STATIC',
    'synchronized' : 'SYNCHRONIZED',
    'void'      : 'VOID'
    }


    tokens = [ "ACCESS", "TYPE", "ID", "VARID", "BODY" ] + reserved.values()


    t_ignore = ' \t\f'
    t_CLASS = r'class'
    t_INTERFACE = r'interface'
    t_IMPLEMENTS = r'implements'
    t_EXTENDS = r'extends'
    t_ABSTRACT = r'abstract'
    t_FINAL = r'final'
    t_STATIC = r'static'
    t_SYNCHRONIZED = r'synchronized'
    t_VOID = r'void'

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_newline2(self,t):
        r'(\r\n)+'
        t.lexer.lineno += len(t.value) / 2


    def t_error(self,t):
        print("Illegal character '{0}' ({1}) in line {2}".format(t.value[0], hex(ord(t.value[0])), t.lexer.lineno))
        t.lexer.skip(1)


    def t_LINE_COMMENT(self,t):
        r'\#.*'
        pass

    def t_BLOCK_COMMENT(self,t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    def t_ACCESS(self, t):
        r'private|protected|public'
        return t

    def t_TYPE(self, t):
        r'\b(int|short|long|float|double|boolean|char|String)\b'
        return t

    def t_ID(self, t):
        r'[A-Z]\w*'
        t.type = Scanner.reserved.get(t.value, 'ID')
        return t

    def t_VARID(self, t):
        r'[a-z_]\w*'
        t.type = Scanner.reserved.get(t.value, 'VARID')
        return t

    def t_BODY(self, t):
        r'{(\n*|.*)*}'
        return t