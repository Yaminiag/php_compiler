from php_lex import symbol_table
import copy

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
    
T_count=0
L_count=0

def temp():
	global T_count
	T_count+=1
	return "t"+str(T_count)
	
def label():
	global L_count
	L_count+=1
	return "L"+str(L_count)
    
class Synth:
	def __init__(self, code, addr=None):
		self.code=code
		self.addr=addr
		
class Inh:
	def __init__(self, inh1, inh2=None, inh3=None):
		self.inh1=inh1
		self.inh2=inh2
		self.inh3=inh3

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
	l=len(list(p))
	if l==2:
		p[1]=str(p[1])
		p[0]=Synth("",p[1])
	if l==3:
		p[1]=str(p[1])
		
	

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : args
    | MultiplicativeExpression '*' args
	| MultiplicativeExpression '/' args
	| MultiplicativeExpression '%' args
    '''
    l=len(list(p))
    if l==2:
    	p[0]=p[1]
    else:
    	addr=temp()
    	code=p[1].code+p[3].code+addr+"="+p[1].addr+p[2]+p[3].addr+"\n"
    	p[0]=Synth(code,addr)
    
		
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression '+' MultiplicativeExpression
        | AdditiveExpression '-' MultiplicativeExpression
    '''
    l=len(list(p))
    if l==2:
    	p[0]=p[1]
    else:
    	addr=temp()
    	code=p[1].code+p[3].code+addr+"="+p[1].addr+p[2]+p[3].addr+"\n"
    	p[0]=Synth(code,addr)
   

def p_arithmeticExp(p):
	''' arithmeticExp : AdditiveExpression
						| MultiplicativeExpression
						
	'''
	p[0] = p[1]

def p_start(p):
	'''start : OPENTAG statement'''
	p[0]=p[2]
	print("\n\nIntermediate 3-Address Code\n")
	print(p[0].code)

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
	p[0]=p[1]
	

def p_statement(p):
	'''statement : states statement
				   | end
	'''
	l=len(list(p))
	if l==3:
		code=p[1].code+p[2].code
		p[0]=Synth(code)
	else:
		p[0]=Synth("")
	
	
def p_assignmentOperator(p):
    '''assignmentOperator : '='
    | ASS_MUL
    | ASS_DIV
    | ASS_MOD
    | ASS_ADD
    | ASS_SUB
    '''
   

def p_params(p):
	'''params : args
			  | args ',' params
	'''
	
def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";"
					| IDENTIFIER '=' '[' params ']' ';'
				  
	'''
	l=len(list(p))
	if l==5:
		code=p[3].code+p[1]+"="+p[3].addr+"\n"
		p[0]=Synth(code)
	
	
def p_postfixExprInc(p):
	'''postfixExprInc : IDENTIFIER OP_INC
	'''
	t=temp()
	code=t+"="+p[1]+"+1\n"+p[1]+"="+t+"\n"
	p[0]=Synth(code)
	
def p_postfixExprDec(p):
	'''postfixExprDec : IDENTIFIER OP_DEC 
	'''
	t=temp()
	code=t+"="+p[1]+"-1\n"+p[1]+"="+t+"\n"
	p[0]=Synth(code)

def p_prefixExprInc(p):
	'''prefixExprInc : OP_INC IDENTIFIER
	'''
	t=temp()
	code=t+"="+p[2]+"+1\n"+p[2]+"="+t+"\n"
	p[0]=Synth(code)

def p_prefixExprDec(p):
	'''prefixExprDec : OP_DEC IDENTIFIER 
	'''
	t=temp()
	code=t+"="+p[2]+"-1\n"+p[2]+"="+t+"\n"
	p[0]=Synth(code)
	

def p_whileLoop(p):
	'''whileLoop : WHILE '(' conditionalExp ')' '{' block '}'
	'''
	#whileLoop's next needs to be known
	l1=label()
	l2=label()
	next="out"
	p[0]=Inh(l2,next,l1)
	
	
def p_forEach(p):
	'''forEach : FOREACH '(' IDENTIFIER AS IDENTIFIER ')' '{' block '}'
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
	code=p[1]
	p[0]=Synth(code)
	

def p_conditionalExp(p):
	'''conditionalExp : condArgs conditionalOp condArgs
					  | condArgs
					  | conditionalExp logicalOp conditionalExp
					  | '(' conditionalExp ')' logicalOp '(' conditionalExp ')'
					  | '(' conditionalExp ')' logicalOp conditionalExp
					  | conditionalExp logicalOp '(' conditionalExp ')'
	'''
	l=len(list(p))
	if l==4:
		code="if "+p[1].addr+p[2].code+p[3].addr+" goto "+p[-1].inh1+"\ngoto "+p[-1].inh2+"\n"
		p[0]=Synth(code)
			

def p_logicalOp(p):
	'''logicalOp : OP_LAND
				 | OP_LOR
				 | OP_XOR
	'''
	code=p[1]
	p[0]=Synth(code)

def p_condArgs(p):
	''' condArgs : IDENTIFIER
				 | arithmeticExp
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
