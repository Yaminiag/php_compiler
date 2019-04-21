symbol_table = {}

keywords = ['array', 'as', 'break', 'case',
			'const', 'continue',
			'do', 'echo', 'else', 'elseif',
			'for', 'foreach','global', 'if',
			'new', 'print', 'require',
			'return', 'static', 'while']

for kw in keywords:
	symbol_table[kw] = {}
	symbol_table[kw]['type'] = "keyword"

def t_OPENTAG(t):
	r"<\?php"
	t.type = "OPENTAG"
	t.lexer.lineno = 0
	return t

def t_CLOSETAG(t):
	r"\?>"
	t.type = "CLOSETAG"
	return t

def t_OP_INC(t):
	r"\+\+"
	t.type = "OP_INC"
	return t

def t_OP_DEC(t):
	r"--"
	t.type = "OP_DEC"
	return t

def t_OP_GE(t):
	r">="
	t.type = "OP_GE"
	return t

def t_OP_LE(t):
	r"<="
	t.type = "OP_LE"
	return t

def t_OP_IDENTICAL(t):
	r"==="
	t.type = "OP_IDENTICAL"
	return t

def t_OP_NOTIDENTICAL(t):
	r"!=="
	t.type = "OP_NOTIDENTICAL"
	return t

def t_OP_EQ(t) :
	r"=="
	t.type = "OP_EQ"
	return t

def t_OP_NE(t) :
	r"!= | <>"
	t.type = "OP_NE"
	return t

def t_OP_LAND(t) :
	r"&& | and"
	t.type = "OP_LAND"
	return t

def t_OP_LOR(t) :
	r"\|\| | or"
	t.type = "OP_LOR"
	return t

def t_OP_XOR(t):
	r"xor"
	t.type = "OP_XOR"
	return t

def t_ASS_MUL(t) :
	r"\*="
	t.type = "ASS_MUL"
	return t

def t_ASS_DIV(t) :
	r"/="
	t.type = "ASS_DIV"
	return t

def t_ASS_MOD(t) :
	r"%="
	t.type = "ASS_MOD"
	return t

def t_ASS_ADD(t) :
	r"\+="
	t.type = "ASS_ADD"
	return t

def t_ASS_SUB(t) :
	r"-="
	t.type = "ASS_SUB"
	return t

#doc comments
def t_COMMENTS(t):
	r'/\*\*(.|\n)*?\*/'
	return t

def t_COMMENT(t) :
	r'/\*(.|\n)*?\*/ | //(.)*\n? | \#(.)*\n?'

def t_BOOL_LITERAL(t) :
	r'[Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee]'
	t.type = "BOOL_LITERAL"
	return t

literals = [';', ',', '+', '-', '*', '/',
			'%','<', '>', '!', '&', '|',
			'(', ')', '{', '}', '=', '[', ']']

def t_KEYWORDS(t):
	r"[A-Za-z_][A-Za-z0-9_]*"
	if t.value in symbol_table:
		if("type" in symbol_table[t.value]):
			if(symbol_table[t.value]["type"] == "keyword"):
				t.type = t.value.upper()
				symbol_table[t.value]["token"] = t
	return t

def t_IDENTIFIER(t):
	r"\$[A-Za-z_][A-Za-z0-9_]*"
	if t.value not in symbol_table:
		symbol_table[t.value] = {}
		symbol_table[t.value]["type"] = "identifier"
		symbol_table[t.value]["token"] = t
		symbol_table[t.value]["valid"] = False
		symbol_table[t.value]["value"] = "None"
	return t

def t_semicolon(t):
	r';'
	t.type = ';'
	return t

def t_comma(t):
	r','
	t.type = ','      
	return t

def t_op_plus(t):
	r'\+'
	t.type = '+'      
	return t

def t_op_minus(t):
	r'-'
	t.type = '-'      
	return t

def t_op_multiply(t):
	r'\*'
	t.type = '*'      
	return t

def t_op_divide(t):
	r'/'
	t.type = '/'      
	return t

def t_op_modulus(t):
	r'%'
	t.type = '%'      
	return t

def t_op_lt(t):
	r'<'
	t.type = '<'      
	return t

def t_op_gt(t):
	r'>'
	t.type = '>'      
	return t

def t_op_not(t):
	r'!'
	t.type = '!'      
	return t

def t_op_and(t):
	r'&'
	t.type = '&'      
	return t

def t_op_or(t):
	r'\|'
	t.type = '|'      
	return t

def t_lparen(t):
	r'\('
	t.type = '('      
	return t

def t_rparen(t):
	r'\)'
	t.type = ')'      
	return t

def t_lbrace(t):
	r'{'
	t.type = '{'      
	return t

def t_rbrace(t):
	r'}'
	t.type = '}'      
	return t

def t_ass(t):
	r'='
	t.type = '='      
	return t
	
def lsquare(t):
	r'['
	t.type='['
	return t

def rsquare(t):
	r']'
	t.type=']'
	return t

# Floating literal
# \d is 0-9
def t_DNUM_LITERAL(t):
	r'(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d+)? | (\d+[Ee][+-]?\d+)'
	t.value = float(t.value)
	return t

# Integer literal
def t_LNUM_LITERAL(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Single quote String literal
def t_SINGLE_STRING(t):
	r"'([^\\']|\\(.|\n))*'" 
	t.lexer.lineno += t.value.count("\n")
	return t

# Double quote string
def t_DOUBLE_STRING(t):
	r'"([^\\"]|\\(.|\n))*"'
	t.lexer.lineno += t.value.count("\n")
	return t

# Ignored characters
# t_OP_DIM = r"\[{ |\t}*\]"
t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s'" % t.value[0]+"line "+str(t.lexer.lineno))
	t.lexer.skip(1)
