from final_lex import symbol_table

tokens = [
'ARRAY', 'AS', 'BREAK', 'CASE',
'CONST', 'CONTINUE',
'DO', 'ECHO', 'ELSE', 'ELSEIF',
'FOR', 'FOREACH','GLOBAL', 'IF',
'NEW', 'PRINT', 'REQUIRE',
'RETURN', 'STATIC', 'WHILE',
"OPENTAG","CLOSETAG",
"OP_INC", "OP_DEC", "OP_IDENTICAL","OP_NOTIDENTICAL",
"OP_GE", "OP_LE", "OP_EQ", "OP_NE",
"OP_LAND", "OP_LOR","OP_XOR",
"ASS_MUL", "ASS_DIV", "ASS_MOD", "ASS_ADD", "ASS_SUB", "ASS_OR", "ASS_AND",
"IDENTIFIER","KEYWORDS",
"SINGLE_STRING","DOUBLE_STRING",
"BOOL_LITERAL", "DNUM_LITERAL","LNUM_LITERAL"
]

start = 'start'

# def p_error(p):
#     print('Syntax error in input! Parser State')

def p_start(p):
	'''start : OPENTAG statement'''

def p_statement(p):
	'''statement : assignment statement
				   | postfixExpr ";" statement
				   | prefixExpr ";" statement
				   | end
	'''
	p[0] = p[1:]

def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";" 
				  | IDENTIFIER assignmentOperator postfixExpr ";"
				  | IDENTIFIER assignmentOperator prefixExpr ";"
	'''
	p[0] = p[1:]

def p_operator(p):
	''' operator : '+'
				 | '-'
				 | '*'
				 | '/'
	'''

def p_assignmentOperator(p):
    '''assignmentOperator : '='
    | ASS_MUL
    | ASS_DIV
    | ASS_MOD
    | ASS_ADD
    | ASS_SUB
    '''
    p[0] = p[1:]

def p_arithmeticExp(p):
	''' arithmeticExp : args operator args
						| args operator postfixExpr
						| args operator prefixExpr
						| args
						| SINGLE_STRING
						| DOUBLE_STRING
	'''
	p[0] = p[1:]

def p_args(p):
	'''args : IDENTIFIER
			| LNUM_LITERAL
			| DNUM_LITERAL
	'''
	p[0] = p[1:]

def p_postfixExpr(p):
	'''postfixExpr : IDENTIFIER OP_INC 
				   | IDENTIFIER OP_DEC 
	'''

def p_prefixExpr(p):
	'''prefixExpr : OP_INC IDENTIFIER  
				   | OP_DEC IDENTIFIER 
	'''

def p_end(p):
	'''end : CLOSETAG'''
