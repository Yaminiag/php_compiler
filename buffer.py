"""def p_function_end(p):
	'''function_end : '}'
	'''
	scope.pop()
	p[0] = p[1:]
	
def p_function(p):
	'''function : block function_end
	'''
	p[0] = p[1:]"""
	
def p_function_begin(p):
	'''function_begin : FUNCTIONWORD FUNCTION_NAME '(' ')' '{' block '}'
	'''
	print(p[:])
	scope.append(flatten(p[2])[0])
	p[0] = p[1:]

def t_FUNCTIONWORD(t):
	r'function'
	t.type = 'FUNCTIONWORD'
	return t
	
else:
		symbol_table[t.value] = {}
		symbol_table[t.value]["type"] = "FUNCTION_NAME"
		symbol_table[t.value]["token"] = t
		symbol_table[t.value]["valid"] = False