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
   'implements': 'IMPLEMENTS',
   'extends'   : 'EXTENDS',
   'private'   : 'PRIVATE',
   'protected' : 'PROTECTED',
   'public'    : 'PUBLIC',
  }


  tokens = [   ] + list(reserved.values())
           

  t_ignore = ' \t\f'

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
