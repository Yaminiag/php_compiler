from final_lex import symbol_table

tokens = [
'ARRAY', 'AS', 'BREAK',
'CONTINUE',
'ECHO', 'ELSE', 'ELSEIF',
'FOREACH','GLOBAL', 'IF',
'NEW', 'PRINT', 'REQUIRE',
'RETURN', 'STATIC', 'WHILE',
"OPENTAG","CLOSETAG",
"OP_INC", "OP_DEC", "OP_IDENTICAL","OP_NOTIDENTICAL",
"OP_GE", "OP_LE", "OP_EQ", "OP_NE",
"OP_LAND", "OP_LOR","OP_XOR",
"ASS_MUL", "ASS_DIV", "ASS_MOD", "ASS_ADD", "ASS_SUB",
"IDENTIFIER","KEYWORDS",
"SINGLE_STRING","DOUBLE_STRING",
"BOOL_LITERAL", "DNUM_LITERAL","LNUM_LITERAL"
]

start = 'start'

# def p_error(p):
#     print('Syntax error in input! Parser State')+

def p_start(p):
	'''start : OPENTAG statement'''

def p_states(p):
	'''states : assignment
			  | postfixExpr ";"
			  | prefixExpr ";"
			  | whileLoop
			  | return
			  | break
			  | continue
			  | echo 
			  | print

	'''

def p_statement(p):
	'''statement : states statement
				   | end
	'''
	p[0] = p[1:]

def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";" 
				  
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
						| args
	'''
	p[0] = p[1:]

def p_args(p):
	'''args : IDENTIFIER
			| LNUM_LITERAL
			| DNUM_LITERAL
			| SINGLE_STRING
			| DOUBLE_STRING
			| BOOL_LITERAL
			| postfixExpr
			| prefixExpr
	'''
	p[0] = p[1:]

def p_postfixExpr(p):
	'''postfixExpr : IDENTIFIER OP_INC 
				   | IDENTIFIER OP_DEC 
	'''
	p[0] = p[1:]

def p_prefixExpr(p):
	'''prefixExpr : OP_INC IDENTIFIER  
				   | OP_DEC IDENTIFIER 
	'''
	p[0] = p[1:]

def p_whileLoop(p):
	'''whileLoop : WHILE '(' conditionalExp ')' '{' block '}'
	'''
def p_conditionalOp(p):
	'''conditionalOp : OP_GE
					 | OP_LE
					 | OP_IDENTICAL
					 | OP_NOTIDENTICAL
					 | OP_EQ
					 | OP_NE
					 | '<'
					 | '>'
	'''

def p_conditionalExp(p):
	'''conditionalExp : condArgs conditionalOp condArgs
					  | condArgs
					  | conditionalExp logicalOp conditionalExp
					  | '(' conditionalExp ')' logicalOp '(' conditionalExp ')'
					  | '(' conditionalExp ')' logicalOp conditionalExp
					  | conditionalExp logicalOp '(' conditionalExp ')'
	'''

def p_logicalOp(p):
	'''logicalOp : OP_LAND
				 | OP_LOR
				 | OP_XOR
	'''

def p_condArgs(p):
	''' condArgs : arithmeticExp
				 | IDENTIFIER
				 | LNUM_LITERAL
				 | DNUM_LITERAL
	'''

def p_block(p):
	'''block : states block
			 |
	'''

def p_return(p):
	'''return : RETURN ";"
			  | RETURN arithmeticExp ";"
	'''
	p[0] = p[1:]

def p_break(p):
	'''break : BREAK ";"
	'''

def p_continue(p):
	'''continue : CONTINUE ";"
	'''

def p_echo(p):
	'''echo : ECHO ";"
			| ECHO arithmeticExp ";"
	'''

def p_print(p):
	'''print : PRINT arithmeticExp ";"
			 | PRINT '(' arithmeticExp ')' ';'
	'''

def p_end(p):
	'''end : CLOSETAG'''