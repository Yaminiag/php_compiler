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

"""def p_error(p):
    print('Syntax error in input! Parser State')"""
	
# def p_modifier(p):
# 	'''modifier: GLOBAL | STATIC
# 	'''
# 	p[0] = p[1:]
	
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

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : args
    | MultiplicativeExpression '*' args
	| MultiplicativeExpression '/' args
	| MultiplicativeExpression '%' args
    '''
    if len(list(p))==4:
        print(p[:])
        t1 = flatten(p[1])[0]
        t2 = flatten(p[3])[0]
        if t1 in symbol_table:
            if symbol_table[t1]['valid']:
                t1 = symbol_table[t1]['value']
            else:
                print("error line: Undeclared variable", t1)
                t1 = symbol_table[t1]['value']
                return

        if t2 in symbol_table:
            if symbol_table[t2]['valid']:
                t2 = symbol_table[t2]['value']
            else:
                print("error line: Undeclared variable", t2)
                t2 = symbol_table[t2]['value']
                return

        if t1 == None:
        	valid = 0
        elif t2 == None:
        	valid = 0
        else:
        	valid = 1
        if valid:
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
        | AdditiveExpression '+' MultiplicativeExpression
        | AdditiveExpression '-' MultiplicativeExpression
    '''
    if len(list(p))==4:
        t1 = flatten(p[1])[0]
        t2 = flatten(p[3])[0]
        if t1 in symbol_table:
            if symbol_table[t1]['valid']:
                t1 = symbol_table[t1]['value']
            else:
                print("error line: Undeclared variable",t1)
                t1 = symbol_table[t1]['value']
                return

        if t2 in symbol_table:
            if symbol_table[t2]['valid']:
                t2 = symbol_table[t2]['value']
            else:
                print("error line: Undeclared variable",t2)
                t2 = symbol_table[t2]['value']
                return

        if t1 == None:
        	valid = 0
        elif t2 == None:
        	valid = 0
        else:
        	valid = 1
        if valid:        
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
			  | forEach
			  | return
			  | break
			  | continue
			  | echo 
			  | print

	'''
	p[0] = p[1:]

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

def p_params(p):
	'''params : args
			  | args ',' params
	'''
	if(len(list(p))==2):
		p[0] = p[1:]
	else:
		x = flatten(p[3])
		p[0] = []
		p[0].append(p[1][0])
		for val in x:
			p[0].append(val)
	
def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";"
					| IDENTIFIER '=' '[' params ']' ';'
				  
	'''
	

	if len(list(p))>5:
		variable = flatten(p[1])[0]
		symbol_table[variable]['valid'] = True
		#p[4], p[6]
		print(p[4])
		#print(flatten(p[4][4])[0])
		#l=[]
		#l.append(flatten(p[4])[0])
		#l.append(flatten(p[6])[0])
		symbol_table[variable]['value']=p[4]
		symbol_table[variable]['type']= "array_identifier"
		
		
	if len(list(p))==5:
		print(p[:])
		variable = flatten(p[1])[0]
		p[0] = symbol_table[variable]['value']
		symbol_table[variable]['valid'] = True
		rhs = flatten(p[3])[0]
		if variable in symbol_table:
			if symbol_table[variable]['valid']:
				pass
				# if symbol_table[variable]['value']!="None":
				# 	rhs = symbol_table[variable]['value']
				# 	print(rhs)
			else:
				print("error line:Undeclared variable",symbol_table[variable]["token"],"   rhs = ", rhs, 'lhs = ',symbol_table[variable]["token"])
		if p[2][0]=='=':
			p[0] = rhs
			
		else:
			if(p[0]== 'None'):
				print("error line: Undeclared variable",symbol_table[variable]["token"],"   rhs = ", rhs, 'lhs = ',symbol_table[variable]["token"])
			else:
				if p[2][0]=='+=':
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
	p[0] = p[1:]
	print(p[0])
	
def p_forEach(p):
	'''forEach : FOREACH '(' IDENTIFIER AS IDENTIFIER ')' '{' block '}'
	'''
	p[0] = p[1:]
	
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
	p[0] = p[1:]

def p_conditionalExp(p):
	'''conditionalExp : condArgs conditionalOp condArgs
					  | condArgs
					  | conditionalExp logicalOp conditionalExp
					  | '(' conditionalExp ')' logicalOp '(' conditionalExp ')'
					  | '(' conditionalExp ')' logicalOp conditionalExp
					  | conditionalExp logicalOp '(' conditionalExp ')'
	'''
	if len(list(p))==4:
		t1 = flatten(p[1])[0]
		if t1 in symbol_table:
			if symbol_table[t1]['valid']:
				t1 = symbol_table[t1]['value']
		t2 = flatten(p[3])[0]
		if t2 in symbol_table:
			if symbol_table[t2]['valid']:
				t2 = symbol_table[t2]['value']
		if t1 == None:
			valid = 0
			print("error line: Invalid type", t1 ,"for",flatten(p[1])[0])
		elif t2 == None:
			valid = 0
			print("error line: Invalid type", t2 ,"for",flatten(p[1])[0])
		else:
			valid = 1
		if valid:
			if p[2][0]=='<':
				p[0] = t1 < t2
			elif p[2][0]=='>':
				p[0] = t1 > t2
			elif p[2][0]=='<=':
				p[0] = t1 <= t2
			elif p[2][0]=='>=':
				p[0] = t1 >= t2
			elif p[2][0]=='==':
				p[0] = t1 == t2
			elif p[2][0]=='!=':
				p[0] = t1 != t2
			elif p[2][0]=='<>':
				p[0] = t1 != t2
			elif p[2][0]=='&&' or p[2][0]=='and':
				p[0] = t1 and t2
			elif p[2][0]=='||' or p[2][0]=='or':
				p[0] = t1 or t2
			print('Cond',p[0])

	else:
		p[0] = p[1:]
	

def p_logicalOp(p):
	'''logicalOp : OP_LAND
				 | OP_LOR
				 | OP_XOR
	'''
	p[0] = p[1:]

def p_condArgs(p):
	''' condArgs : arithmeticExp
				 | IDENTIFIER
				 | LNUM_LITERAL
				 | DNUM_LITERAL
	'''
	p[0] = p[1:]

def p_block(p):
	'''block : states block
			 |
	'''
	p[0] = p[1:]

def p_return(p):
	'''return : RETURN ";"
			  | RETURN arithmeticExp ";"
	'''
	p[0] = p[1:]

def p_break(p):
	'''break : BREAK ";"
	'''
	p[0] = p[1:]

def p_continue(p):
	'''continue : CONTINUE ";"
	'''
	p[0] = p[1:]

def p_echo(p):
	'''echo : ECHO ";"
			| ECHO arithmeticExp ";"
	'''
	p[0] = p[1:]

def p_print(p):
	'''print : PRINT arithmeticExp ";"
			 | PRINT '(' arithmeticExp ')' ';'
	'''
	p[0] = p[1:]

def p_end(p):
	'''end : CLOSETAG'''