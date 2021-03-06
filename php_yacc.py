from php_lex import symbol_table
import copy



class Node: 
	def __init__(self,type,children=None):
          self.type = type
          if children:
               self.children = children
          else:
               self.children = [ ]
	def PrintTree(self):
 		print(self.type)
 		for i in self.children:
 			if i is not None:
 				#print(i)
 				# print(i.children)
 				i.PrintTree()
	    	
	def set(self, children):
		self.children = children


root=Node("START")

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
	
def p_args(p):
	'''args : IDENTIFIER
			| LNUM_LITERAL
			| DNUM_LITERAL
			| SINGLE_STRING
			| DOUBLE_STRING
			| BOOL_LITERAL
			| IDENTIFIER OP_INC
			| IDENTIFIER OP_DEC
			| OP_INC IDENTIFIER
			| OP_DEC IDENTIFIER
	'''
	if len(list(p))==3:
		lc = Node(p[1])
		rc = Node(p[2])
		p[0] = Node("INC_DEC",[lc,rc])
	else:
		rc=Node(p[1])
		# print(p[1].children)
		p[0] =rc

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : args
    | MultiplicativeExpression '*' args
	| MultiplicativeExpression '/' args
	| MultiplicativeExpression '%' args
    '''
    # if len(list(p))==4:
    #     print(p[:])
    #     t1 = flatten(p[1])[0]
    #     t2 = flatten(p[3])[0]
    #     if t1 in symbol_table:
    #         if symbol_table[t1]['valid']:
    #             t1 = symbol_table[t1]['value']
    #         else:
    #             print("error line: Undeclared variable", t1)
    #             t1 = symbol_table[t1]['value']
    #             return

    #     if t2 in symbol_table:
    #         if symbol_table[t2]['valid']:
    #             t2 = symbol_table[t2]['value']
    #         else:
    #             print("error line: Undeclared variable", t2)
    #             t2 = symbol_table[t2]['value']
    #             return

    #     if t1 == None:
    #     	valid = 0
    #     elif t2 == None:
    #     	valid = 0
    #     else:
    #     	valid = 1
    #     if valid:
	   #      if p[2]=='*':
	   #          p[0] = t1*t2
	   #      elif p[2]=='/':
	   #          p[0] = t1/t2
	   #      elif p[2]=='%':
	   #          p[0] = t1%t2
    # else:
    #     p[0] = p[1:]
    if len(list(p))==4:
    	p[0]=Node(p[2],[p[1],p[3]])
    else:
    	# print(p[1])
    	p[0]=p[1]

		
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression '+' MultiplicativeExpression
        | AdditiveExpression '-' MultiplicativeExpression
    '''
    # if len(list(p))==4:
    #     t1 = flatten(p[1])[0]
    #     t2 = flatten(p[3])[0]
    #     if t1 in symbol_table:
    #         if symbol_table[t1]['valid']:
    #             t1 = symbol_table[t1]['value']
    #         else:
    #             print("error line: Undeclared variable",t1)
    #             t1 = symbol_table[t1]['value']
    #             return

    #     if t2 in symbol_table:
    #         if symbol_table[t2]['valid']:
    #             t2 = symbol_table[t2]['value']
    #         else:
    #             print("error line: Undeclared variable",t2)
    #             t2 = symbol_table[t2]['value']
    #             return

    #     if t1 == None:
    #     	valid = 0
    #     elif t2 == None:
    #     	valid = 0
    #     else:
    #     	valid = 1
    #     if valid:        
	   #      if p[2]=='+':
	   #          p[0] = t1+t2
	   #      elif p[2]=='-':
	   #          p[0] = t1-t2
    # else:
    #     p[0] = p[1:]
    if len(list(p))==4:
    	#print(p[2])
    	#print(p[1],p[3])
    	p[0]=Node(p[2],[p[1],p[3]])
    else:
    	# print(p[1])
    	p[0]=p[1]
    



def p_arithmeticExp(p):
	''' arithmeticExp : AdditiveExpression
						| MultiplicativeExpression
						
	'''
	# print(p[1])
	p[0] = p[1]


def p_start(p):
	'''start : OPENTAG statement'''
	lc=Node(p[1])
	root.set([lc,p[2]])
	root.PrintTree()

def p_states(p):
	'''states : assignment
			  | postfixExprInc ";"
			  | postfixExprDec ";"
			  | prefixExprInc ";"
			  | prefixExprDec ";"
			  | whileLoop
			  | forEach
			  | return
			  | break
			  | continue
			  | echo 
			  | print

	'''
	if len(list(p))!=2:
		rc=Node(p[2])
		p[0]=Node("EXPR",[p[1],rc]) #postfix
	else:
		#val=str(p[1])
		p[0]=Node("EXPR",[p[1]])

def p_statement(p):
	'''statement : states statement
				   | end
	'''
	if(len(list(p))==3):
		p[0]=Node("SEQ",[p[1],p[2]])
	else:
		p[0]=Node("END")
	
def p_assignmentOperator(p):
    '''assignmentOperator : '='
    | ASS_MUL
    | ASS_DIV
    | ASS_MOD
    | ASS_ADD
    | ASS_SUB
    '''
    rc = Node(p[1])
    p[0] = rc

def p_params(p):
	'''params : args
			  | args ',' params
	'''
	if(len(list(p))==2):
		p[0] = p[1]
	else:
		# x = flatten(p[3])
		# p[0] = []
		# p[0].append(p[1][0])
		# for val in x:
		# 	p[0].append(val)
		rc = Node(p[2])
		p[0] = Node("PARAMS",[p[1],rc,p[3]])
	
def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";"
					| IDENTIFIER '=' '[' params ']' ';'
				  
	'''
	
	if len(list(p)) == 5:
		lc = Node(p[1])
		rc = Node(p[4])
		print(p[3])
		p[0] = Node("ASSIGNMENT",[lc,p[2],p[3],rc])
	else:
		c1 = Node(p[1])
		c2 = Node(p[2])
		c3 = Node(p[3])
		c5 = Node(p[5])
		c6 = Node(p[6])
		p[0] = Node("ASSIGNMENT",[c1,c2,c3,p[4],c5,c6])

	# if len(list(p))>5:
	# 	# variable = flatten(p[1])[0]
	# 	# symbol_table[variable]['valid'] = True
	# 	# print(p[4])
	# 	# symbol_table[variable]['value']=p[4]
	# 	# symbol_table[variable]['type']= "array_identifier"
		
		
	# if len(list(p))==5:
	# 	print(p[:])
	# 	variable = flatten(p[1])[0]
	# 	p[0] = symbol_table[variable]['value']
	# 	symbol_table[variable]['valid'] = True
	# 	rhs = flatten(p[3])[0]
	# 	if variable in symbol_table:
	# 		if symbol_table[variable]['valid']:
	# 			pass
	# 			# if symbol_table[variable]['value']!="None":
	# 			# 	rhs = symbol_table[variable]['value']
	# 			# 	print(rhs)
	# 		else:
	# 			print("error line:Undeclared variable",symbol_table[variable]["token"],"   rhs = ", rhs, 'lhs = ',symbol_table[variable]["token"])
	# 	if p[2][0]=='=':
	# 		p[0] = rhs
			
	# 	else:
	# 		if(p[0]== 'None'):
	# 			print("error line: Undeclared variable",symbol_table[variable]["token"],"   rhs = ", rhs, 'lhs = ',symbol_table[variable]["token"])
	# 		else:
	# 			if p[2][0]=='+=':
	# 				p[0] += rhs
	# 			elif p[2][0]=='-=':
	# 				p[0] -= rhs             
	# 			elif p[2][0]=='*=':
	# 				p[0] *= rhs
	# 			elif p[2][0]=='/=':
	# 				p[0] /= rhs
	# 			elif p[2][0]=='%=':
	# 				p[0] %= rhs
	# 	symbol_table[variable]['value'] = p[0]
	# else:
	# 	p[0] = p[1:]

def p_postfixExprInc(p):
	'''postfixExprInc : IDENTIFIER OP_INC
	'''

	# if len(list(p))==3:
	# 	variable = flatten(p[1])[0]
	# 	if symbol_table[variable]['value']== "None":
	# 		#error
	# 		symbol_table[variable]['value']=0
	# 	symbol_table[variable]['value']+=1
	# else:
	# 	p[0] = p[1:]
	lc = Node(p[1])
	rc = Node(p[2])
	# print(lc,rc)
	p[0] = Node("POSTFIXINC",[lc,rc])
	# print(p[0].children)
	
def p_postfixExprDec(p):
	'''postfixExprDec : IDENTIFIER OP_DEC 
	'''
	# if len(list(p))==3:
	# 	variable = flatten(p[1])[0]
	# 	if symbol_table[variable]['value']== "None":
	# 		#error
	# 		symbol_table[variable]['value']=0
	# 	symbol_table[variable]['value']-=1
	# else:
	# 	p[0] = p[1:]
	lc = Node(p[1])
	rc = Node(p[2])
	p[0] = Node("POSTFIXDEC",[lc,rc])

def p_prefixExprInc(p):
	'''prefixExprInc : OP_INC IDENTIFIER
	'''
	# if len(list(p))==3:
	# 	variable = flatten(p[2])[0]
	# 	if symbol_table[variable]['value']== "None":
	# 		#error
	# 		symbol_table[variable]['value']=0
	# 	symbol_table[variable]['value']+=1
	# else:
	# 	p[0] = p[1:]
	lc = Node(p[1])
	rc = Node(p[2])
	p[0] = Node("PREFIXINC",[lc,rc])

def p_prefixExprDec(p):
	'''prefixExprDec : OP_DEC IDENTIFIER 
	'''
	# if len(list(p))==3:
	# 	variable = flatten(p[2])[0]
	# 	if symbol_table[variable]['value']== "None":
	# 		#error
	# 		symbol_table[variable]['value']=0
	# 	symbol_table[variable]['value']-=1
	# else:
	# 	p[0] = p[1:]
	lc = Node(p[1])
	rc = Node(p[2])
	p[0] = Node("PREFIXDEC",[lc,rc])

def p_whileLoop(p):
	'''whileLoop : WHILE '(' conditionalExp ')' '{' block '}'
	'''
	c1 = Node(p[1])
	c2 = Node(p[2])
	c4 = Node(p[4])
	c5 = Node(p[5])
	c7 = Node(p[7])
	p[0] = Node("WHILE",[c1,c2,p[3],c4,c5,p[6],c7])
	# print(p[0])
	
def p_forEach(p):
	'''forEach : FOREACH '(' IDENTIFIER AS IDENTIFIER ')' '{' block '}'
	'''
	p[0] = 
	
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
	lc = Node(p[1])
	p[0] = lc

def p_conditionalExp(p):
	'''conditionalExp : condArgs conditionalOp condArgs
					  | condArgs
					  | conditionalExp logicalOp conditionalExp
					  | '(' conditionalExp ')' logicalOp '(' conditionalExp ')'
					  | '(' conditionalExp ')' logicalOp conditionalExp
					  | conditionalExp logicalOp '(' conditionalExp ')'
	'''

	if len(list(p))==4:
		p[0] = Node("COND",[p[1],p[2],p[3]])
	# print(p[0])
	# if len(list(p))==4:
	# 	t1 = flatten(p[1])[0]
	# 	if t1 in symbol_table:
	# 		if symbol_table[t1]['valid']:
	# 			t1 = symbol_table[t1]['value']
	# 	t2 = flatten(p[3])[0]
	# 	if t2 in symbol_table:
	# 		if symbol_table[t2]['valid']:
	# 			t2 = symbol_table[t2]['value']
	# 	if t1 == None:
	# 		valid = 0
	# 		print("error line: Invalid type", t1 ,"for",flatten(p[1])[0])
	# 	elif t2 == None:
	# 		valid = 0
	# 		print("error line: Invalid type", t2 ,"for",flatten(p[1])[0])
	# 	else:
	# 		valid = 1
	# 	if valid:
	# 		if p[2][0]=='<':
	# 			p[0] = t1 < t2
	# 		elif p[2][0]=='>':
	# 			p[0] = t1 > t2
	# 		elif p[2][0]=='<=':
	# 			p[0] = t1 <= t2
	# 		elif p[2][0]=='>=':
	# 			p[0] = t1 >= t2
	# 		elif p[2][0]=='==':
	# 			p[0] = t1 == t2
	# 		elif p[2][0]=='!=':
	# 			p[0] = t1 != t2
	# 		elif p[2][0]=='<>':
	# 			p[0] = t1 != t2
	# 		elif p[2][0]=='&&' or p[2][0]=='and':
	# 			p[0] = t1 and t2
	# 		elif p[2][0]=='||' or p[2][0]=='or':
	# 			p[0] = t1 or t2
	# 		print('Cond',p[0])

	# else:
	# 	p[0] = p[1:]
	

def p_logicalOp(p):
	'''logicalOp : OP_LAND
				 | OP_LOR
				 | OP_XOR
	'''
	p[0] = p[1:]

def p_condArgs(p):
	''' condArgs : IDENTIFIER
				 | arithmeticExp
				 | LNUM_LITERAL
				 | DNUM_LITERAL
	'''
	if(type(p[1])=='str'):
		lc = Node(p[1])
		print(p[1])
		p[0] = lc
	else:
		p[0] = p[1]
	#print(type(p[1]))
	

def p_block(p):
	'''block : states block
			 |
	'''
	if len(list(p))==3:
		p[0] = Node("BLOCK",[p[1],p[2]])
	else:
		p[0] = None

def p_return(p):
	'''return : RETURN ";"
			  | RETURN arithmeticExp ";"
	'''
	if(len(list(p))==3):
		lc=Node(p[1])
		rc=Node(p[2])
		p[0] = Node("RET",[lc,rc])
	else:
		lc=Node(p[1])
		rc=Node(p[3])
		p[0]=Node("RET",[lc,p[2],rc])

def p_break(p):
	'''break : BREAK ";"
	'''
	rc = Node(p[2])
	p[0]=Node(p[1],[p[1],rc])

def p_continue(p):
	'''continue : CONTINUE ";"
	'''
	rc = Node(p[2])
	p[0] = Node(p[1],[p[1],rc])

def p_echo(p):
	'''echo : ECHO ";"
			| ECHO arithmeticExp ";"
	'''
	if(len(list(p))==3):
		lc=Node(p[1])
		rc=Node(p[2])
		p[0] = Node("ECHO",[lc,rc])
	else:
		lc=Node(p[1])
		rc=Node(p[3])
		p[0]=Node("ECHO",[lc,p[2],rc])

def p_print(p):
	'''print : PRINT arithmeticExp ";"
			 | PRINT '(' arithmeticExp ')' ';'
	'''

def p_end(p):
 	'''end : CLOSETAG'''
 	#root.PrintTree()
