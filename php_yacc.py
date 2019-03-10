from php_lex import symbol_table

def flatten(l):
    output = []
    def removeNestings(l):
        for i in l:
            if type(i) == list:
                removeNestings(i)
            else:
                output.append(i)
    if type(l) == list:
        removeNestings(l)
    else:
        output.append(l)
    return output

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

def p_error(p):
    print('Syntax error in input! Parser State')
	
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
	
def p_muloperator(p):
	''' muloperator : '*'
				 | '/'
				 | '%'
	'''
	
def p_addoperator(p):
	''' addoperator : '+'
				 | '-'
	'''

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : args
    | MultiplicativeExpression muloperator args
    '''
    if len(list(p))==4:
        print(p[:])
        t1 = flatten(p[1])[0]
        t2 = flatten(p[3])[0]
        if t1 in symbol_table:
            if symbol_table[t1]['valid'] or not symbol_table[t1]['valid']:
                t1 = symbol_table[t1]['value']
            else:
                print("error line:",symbol_table[t1]["token"],"   rhs = ", t1)

        if t2 in symbol_table:
            if symbol_table[t2]['valid'] or not symbol_table[t2]['valid']:
                t2 = symbol_table[t2]['value']
            else:
                print("error line:",symbol_table[t2]["token"],"   rhs = ", t2)

        if p[2]=='*':
            p[0] = t1*t2
        elif p[2]=='/':
            p[0] = t1/t2
        elif p[2]=='%':
            p[0] = t1%t2
    else:
        p[0] = p[1:]
		
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression addoperator MultiplicativeExpression
    '''
    if len(list(p))==4:
        t1 = flatten(p[1])[0]
        t2 = flatten(p[3])[0]
        if t1 in symbol_table:
            if symbol_table[t1]['valid'] or not symbol_table[t1]['valid']:
                t1 = symbol_table[t1]['value']
            else:
                print("error line:",symbol_table[t1]["token"],"   rhs = ", t1)

        if t2 in symbol_table:
            if symbol_table[t2]['valid'] or not symbol_table[t2]['valid']:
                t2 = symbol_table[t2]['value']
            else:
                print("error line:",symbol_table[t2]["token"],"   rhs = ", t2)
                
        if p[2]=='+':
            p[0] = t1+t2
        elif p[2]=='-':
            p[0] = t1-t2
    else:
        p[0] = p[1:]	

def p_arithmeticExp(p):
	''' arithmeticExp : AdditiveExpression
						| MultiplicativeExpression
	'''
	p[0] = p[1:]


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
	
def p_assignmentOperator(p):
    '''assignmentOperator : '='
    | ASS_MUL
    | ASS_DIV
    | ASS_MOD
    | ASS_ADD
    | ASS_SUB
    '''
    p[0] = p[1:]

def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";" 
				  
	'''
	#length will be 5 because semicolon is counted, don't forget!!!
	if len(list(p))==5:
		variable = flatten(p[1])[0]
		p[0] = symbol_table[variable]['value']
		rhs = flatten(p[3])[0]
		if rhs in symbol_table:
			if symbol_table[rhs]['valid'] or not symbol_table[rhs]['valid']:
				rhs = symbol_table[rhs]['value']
			else:
				print("error line:",symbol_table[rhs]["token"],"   rhs = ", rhs, 'lhs = ',symbol_table[variable]["token"])
		if p[2][0]=='=':
			p[0] = rhs
		elif p[2][0]=='+=':
			p[0] += rhs
		elif p[2][0]=='-=':
			p[0] -= rhs             
		elif p[2][0]=='*=':
			p[0] *= rhs
		elif p[2][0]=='/=':
			p[0] /= rhs
		elif p[2][0]=='%=':
			p[0] %= rhs
		symbol_table[variable]['value'] = p[0]
	else:
		p[0] = p[1:]

def p_postfixExprInc(p):
	'''postfixExpr : IDENTIFIER OP_INC
	'''
	if len(list(p))==3:
		variable = flatten(p[1])[0]
		if symbol_table[variable]['value']== "None":
			#error
			symbol_table[variable]['value']=0
		symbol_table[variable]['value']+=1
	else:
		p[0] = p[1:]
	
def p_postfixExprDec(p):
	'''postfixExpr : IDENTIFIER OP_DEC 
	'''
	if len(list(p))==3:
		variable = flatten(p[1])[0]
		if symbol_table[variable]['value']== "None":
			#error
			symbol_table[variable]['value']=0
		symbol_table[variable]['value']-=1
	else:
		p[0] = p[1:]

def p_prefixExprInc(p):
	'''prefixExpr : OP_INC IDENTIFIER
	'''
	if len(list(p))==3:
		variable = flatten(p[2])[0]
		if symbol_table[variable]['value']== "None":
			#error
			symbol_table[variable]['value']=0
		symbol_table[variable]['value']+=1
	else:
		p[0] = p[1:]

def p_prefixExprDec(p):
	'''prefixExpr : OP_DEC IDENTIFIER 
	'''
	if len(list(p))==3:
		variable = flatten(p[2])[0]
		if symbol_table[variable]['value']== "None":
			#error
			symbol_table[variable]['value']=0
		symbol_table[variable]['value']-=1
	else:
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