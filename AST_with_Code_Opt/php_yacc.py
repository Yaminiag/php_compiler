from php_lex import symbol_table
import copy
import re

stored_constants=dict()
stored_copies=dict()

class Node:

	assign_lhs=False
	 
	def __init__(self,type,children=None):
          self.type = type
          if children:
               self.children = children
          else:
               self.children = [ ]
    
	def PrintTree(self):
 		ch=self.children
 		if len(ch)==0:
 			print(self.type)
 		if len(ch)==2:
 			if ch[0] is not None:
 				ch[0].PrintTree()
 			print(self.type)
 			if ch[1] is not None:
 				ch[1].PrintTree()
 		if len(ch)==3:
	 		if ch[0] is not None:
	 				ch[0].PrintTree()
 			if ch[1] is not None:
 				ch[1].PrintTree()
 			print(self.type)
 			if ch[2] is not None:
 				ch[2].PrintTree()
 				
 	def set_assign_lhs(self):
 		self.assign_lhs=True    	
 				
 	def indent_tree(self, level=0):
		print '\t' * level + repr(self.type)
		for child in self.children:
			if child is not None:
				child.indent_tree(level+1)
	    	
	def set(self, children):
		self.children = children
		
	def calc(self, s1, s2):
		if self.type=="+":
			ans=s1.type+s2.type
		elif self.type=="-":
			ans=s1.type-s2.type
		elif self.type=="*":
			ans=s1.type*s2.type
		elif self.type=="/":
		#division in PHP - returns float unless both operands are integers and division results in integer
			ans=float(s1.type)/float(s2.type)
			if ans==int(ans):
				ans=int(ans)
		elif self.type=="%":
			ans=s1.type%s2.type
		return ans
	
	def unfold_incdec(self):
		ch=self.children
		for c in ch:
			c.unfold_incdec()
		incdec=["POSTFIXINC","POSTFIXDEC","PREFIXINC","PREFIXDEC"]
		if self.type in incdec:
			op=""
			if "INC" in self.type:
				op="+"
			else:
				op="-"
			n_1=Node(1)
			var=self.children[0]
			opnode=Node(op,[var,n_1])
			self.type="="
			lhs=Node(var.type)
			lhs.set_assign_lhs()
			self.set([lhs,opnode])
		
	# def copy_propagation(self):
	# 	global stored_copies
	# 	ch=self.children
	# 	stops=["WHILE", "FOREACH"]
	# 	for c in ch:
	# 		if c.type not in stops and c.type!="=":
	# 			c.copy_propagation()
	# 		elif c.type=="=":
	# 			var=c.children[0].type
	# 			val=c.children[1].type
	# 			if isinstance(val, str) and val[0]=="$":
	# 				stored_copies[var]=val
	# 				print(stored_copies)
	# 			else:
	# 				c.copy_propagation()
	# 		else:
	# 			stored_copies=dict()
	# 			c.copy_propagation()
						
	# 	for c in ch:
	# 		if c.type in stored_copies and c.assign_lhs==False:
	# 			var=c.type
	# 			val=stored_copies[var]
	# 			while val in stored_copies:
	# 				var=val
	# 				val=stored_copies[var]
	# 			c.type=stored_copies[var]
	# 	if self.type=="=":
	# 		var=ch[0].type
	# 		val=ch[1].type
	# 		if isinstance(val, str) and val[0]=="$":
	# 			stored_copies[var]=val
		
	def constant_folding(self):
		#to add string concatenation
		ch=self.children
		if len(ch)==0:
			return
		else:
			for c in ch:
				c.constant_folding()
		arith="+-*/%"
		if self.type in arith:
			s1=ch[0]
			s2=ch[1]
			v1=isinstance(s1.type,(int,float,long))
			v2=isinstance(s2.type,(int,float,long))
			if v1 and v2:
				ans=self.calc(s1,s2)
				self.type=ans
				#remove children after folding
				self.set([])
				
	def constant_propagation(self):
		global stored_constants
		global symbol_table
		ch=self.children
		stops=["WHILE", "FOREACH"]
		for c in ch:
			c.constant_folding()
			if c.type not in stops and c.type!="=":
				c.constant_propagation()
			elif c.type=="=":
				var=c.children[0].type
				val=c.children[1].type
				if isinstance(val, (int, float, long)):
					symbol_table[var]['valid']='True'
					symbol_table[var]['value']=val
				else:

					c.constant_propagation()
			else:
				for symbol in symbol_table:
						symbol_table[symbol]['valid']='False'
				c.constant_propagation()
				
			c.constant_folding()
		for c in ch:
			if c.type in symbol_table and c.assign_lhs==False and symbol_table[c.type]['valid']=='True':
				c.type=symbol_table[c.type]['value']
		if self.type=="=":
			var=ch[0].type
			val=ch[1].type
			if isinstance(val, (int, float, long)):
				symbol_table[var]['valid']='True'
				symbol_table[var]['value']=val
		
	def gen_icg(self):	
		ch=self.children
		if len(ch)==0:
			stops=["RETURN", "break", "continue"]
			if self.type in stops:
				t=None
				return Synth(self.type,t)
			return Synth("",self.type)
			
		if self.type=="WHILE":
			l1=label() #top of while
			l2=label() #code inside while
			l3=label() #outside while
			s1=ch[0].gen_icg()
			code=l1+": "+s1.code+"goto "+l2+"\ngoto "+l3+"\n"
			s2=ch[1].gen_icg()
			t=None
			if "break" in s2.code:
				parts=s2.code.split("break")
				s2.code=parts[0]+"goto "+l3+"\n"+parts[1]
			elif "continue" in s2.code:	
				parts=s2.code.split("continue")
				s2.code=parts[0]+"goto "+l1+"\n"+parts[1]
			code=code+l2+": "+s2.code+"goto "+l1+"\n"+l3+": "
			return Synth(code, t)

		# len(ch)==3 for FOREACH
		if len(ch)==2:
			#Synth objects
			s1=ch[0].gen_icg()
			s2=ch[1].gen_icg()
			arith="+-*/%"
			logic="<> <= >= == !="
			t=""
			code=""
			if self.type=="=":
				t=None
				s1.addr=str(s1.addr)
				s2.addr=str(s2.addr)
				code=s1.code+s2.code+s1.addr+"="+s2.addr+"\n"
			elif self.type in arith:
				t=temp()
				s1.addr=str(s1.addr)
				s2.addr=str(s2.addr)
				code=s1.code+s2.code+t+"="+s1.addr+self.type+s2.addr+"\n"
			elif self.type=="SEQ":
				t=None
				code=s1.code+s2.code
			elif self.type in logic:
				t=None
				s1.addr=str(s1.addr)
				s2.addr=str(s2.addr)
				code=s1.code+s2.code+"if "+s1.addr+self.type+s2.addr+" "			
			return Synth(code,t)
		
		if len(ch)==1:
			t=""
			code=""
			s1=ch[0].gen_icg()
			incdec=["POSTFIXINC","POSTFIXDEC","PREFIXINC","PREFIXDEC"]
			prints=["PRINT","ECHO", "RETURN"]
			if self.type in incdec:
				t=None
				op=""
				if "INC" in self.type:
					op="+"
				else:
					op="-"
				code=str(s1.addr)+"="+str(s1.addr)+op+"1\n"
			elif self.type in prints:
				t=None
				code=self.type.lower()+" "+s1.addr+"\n"
			elif self.type=="SEQ":
				t=None
				code=s1.code
			elif self.type=="PROGRAM":
				t=None
				code=s1.code
			return Synth(code,t)
		
			
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


root=Node("PROGRAM")

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
		p[0] =rc

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : args
    | MultiplicativeExpression '*' args
	| MultiplicativeExpression '/' args
	| MultiplicativeExpression '%' args
    '''
    
    if len(list(p))==4:
    	p[0]=Node(p[2],[p[1],p[3]])
    else:
    	p[0]=p[1]

		
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression '+' MultiplicativeExpression
        | AdditiveExpression '-' MultiplicativeExpression
    '''
    if len(list(p))==4:
    	p[0]=Node(p[2],[p[1],p[3]])
    else:
    	p[0]=p[1]
    



def p_arithmeticExp(p):
	''' arithmeticExp : AdditiveExpression
						| MultiplicativeExpression
						
	'''
	p[0] = p[1]


def p_start(p):
	'''start : OPENTAG statement'''
	root.set([p[2]])
	print("\n\nAbstract Syntax Tree\n")
	root.indent_tree()
	print("\n\nAfter Copy Propagation\n")
	# root.copy_propagation()
	root.indent_tree()
	print("\n\nAfter Constant Folding and Propagation\n")
	root.unfold_incdec()
	root.constant_propagation()
	root.indent_tree()
	print("\n\nIntermediate 3-Address Code\n")
	S=root.gen_icg()
	print(S.code)

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
		p[0]=p[1]
	else:
		p[0]=p[1]

def p_statement(p):
	'''statement : states statement
				   | end
	'''
	if len(list(p))==3:
		if p[2] is not None:
			p[0] = Node("SEQ",[p[1],p[2]])
		else:
			p[0] = Node("SEQ",[p[1]])
	else:
		#print("reached end")
		p[0] = None
	
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
		p[0] = Node("PARAMS",[p[1],p[3]])
	
def p_assignment(p):
	'''assignment : IDENTIFIER assignmentOperator arithmeticExp ";"
					| IDENTIFIER '=' '[' params ']' ';'
				  
	'''
	
	if len(list(p)) == 5:
		lc = Node(p[1])
		lc.set_assign_lhs()
		p[0] = Node("=",[lc,p[3]])
	else:
		c1 = Node(p[1])
		c1.set_assign_lhs()
		p[0] = Node("=",[c1,p[4]])

def p_postfixExprInc(p):
	'''postfixExprInc : IDENTIFIER OP_INC
	'''
	lc = Node(p[1])
	p[0] = Node("POSTFIXINC",[lc])
	
def p_postfixExprDec(p):
	'''postfixExprDec : IDENTIFIER OP_DEC 
	'''
	lc = Node(p[1])
	p[0] = Node("POSTFIXDEC",[lc])

def p_prefixExprInc(p):
	'''prefixExprInc : OP_INC IDENTIFIER
	'''
	lc = Node(p[2])
	p[0] = Node("PREFIXINC",[lc])

def p_prefixExprDec(p):
	'''prefixExprDec : OP_DEC IDENTIFIER 
	'''
	lc = Node(p[2])
	p[0] = Node("PREFIXDEC",[lc])

def p_whileLoop(p):
	'''whileLoop : WHILE '(' conditionalExp ')' '{' block '}'
	'''
	p[0] = Node("WHILE",[p[3],p[6]])
	
def p_forEach(p):
	'''forEach : FOREACH '(' IDENTIFIER AS IDENTIFIER ')' '{' block '}'
	'''
	id1=Node(p[3])
	id2=Node(p[5])
	p[0] = Node("FOREACH",[id1,id2,p[8]])
	
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
	p[0] = p[1]

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
		p[0] = Node(p[2],[p[1],p[3]])
	elif l==7:
		p[0] = Node(p[4],[p[2],p[6]])
	

def p_logicalOp(p):
	'''logicalOp : OP_LAND
				 | OP_LOR
				 | OP_XOR
	'''

def p_condArgs(p):
	''' condArgs : IDENTIFIER
				 | arithmeticExp
				 | LNUM_LITERAL
				 | DNUM_LITERAL
	'''
	if(type(p[1])=='str'):
		lc = Node(p[1])
		p[0] = lc
	else:
		p[0] = p[1]
	

def p_block(p):
	'''block : states block
			 |
	'''
	if len(list(p))==3:
		if p[2] is not None:
			p[0] = Node("SEQ",[p[1],p[2]])
		else:
			p[0] = Node("SEQ",[p[1]])
	else:
		p[0] = None

def p_return(p):
	'''return : RETURN ";"
			  | RETURN arithmeticExp ";"
	'''
	if(len(list(p))==3):
		p[0] = Node("RETURN")
	else:
		p[0]=Node("RETURN",[p[2]])

def p_break(p):
	'''break : BREAK ";"
	'''
	p[0]=Node(p[1])

def p_continue(p):
	'''continue : CONTINUE ";"
	'''
	p[0] = Node(p[1])

def p_echo(p):
	'''echo : ECHO ";"
			| ECHO arithmeticExp ";"
	'''
	if(len(list(p))==3):
		p[0] = Node("ECHO")
	else:
		p[0]=Node("ECHO",[p[2]])

def p_print(p):
	'''print : PRINT arithmeticExp ";"
			 | PRINT '(' arithmeticExp ')' ';'
	'''
	if(len(list(p))==4):
		p[0]=Node("PRINT",[p[2]])
	else:
		p[0]=Node("PRINT",[p[3]])

def p_end(p):
 	'''end : CLOSETAG'''
