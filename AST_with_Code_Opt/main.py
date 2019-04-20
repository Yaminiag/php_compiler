from php_lex import *
from php_yacc import *

import sys
import ply.lex as lex
import ply.yacc as yacc

lex.lex(debug=0)
parser = yacc.yacc(debug=0)

with open('input.php','r') as f:
	input_str = f.read()

print("\n\n\n========Tokens Generated============")
lex.input(input_str)
 # Tokenize
while True:
 tok = lex.token()
 if not tok:
	 break      # No more input
 print(tok)

x = parser.parse(input_str)

print("\n\n\n============Symbol Table=============")
for symbol in symbol_table:
	if("token" in symbol_table[symbol]):
		print(symbol_table[symbol])
