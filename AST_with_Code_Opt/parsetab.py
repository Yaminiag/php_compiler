
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startARRAY AS ASS_ADD ASS_DIV ASS_MOD ASS_MUL ASS_SUB BOOL_LITERAL BREAK CLOSETAG CONTINUE DNUM_LITERAL DOUBLE_STRING ECHO ELSE ELSEIF FOREACH GLOBAL IDENTIFIER IF KEYWORDS LNUM_LITERAL NEW OPENTAG OP_DEC OP_EQ OP_GE OP_IDENTICAL OP_INC OP_LAND OP_LE OP_LOR OP_NE OP_NOTIDENTICAL OP_XOR PRINT REQUIRE RETURN SINGLE_STRING STATIC WHILEargs : IDENTIFIER\n\t\t\t| LNUM_LITERAL\n\t\t\t| DNUM_LITERAL\n\t\t\t| SINGLE_STRING\n\t\t\t| DOUBLE_STRING\n\t\t\t| BOOL_LITERAL\n\t\t\t| IDENTIFIER OP_INC\n\t\t\t| IDENTIFIER OP_DEC\n\t\t\t| OP_INC IDENTIFIER\n\t\t\t| OP_DEC IDENTIFIER\n\tMultiplicativeExpression : args\n    | MultiplicativeExpression \'*\' args\n\t| MultiplicativeExpression \'/\' args\n\t| MultiplicativeExpression \'%\' args\n    AdditiveExpression : MultiplicativeExpression\n        | AdditiveExpression \'+\' MultiplicativeExpression\n        | AdditiveExpression \'-\' MultiplicativeExpression\n     arithmeticExp : AdditiveExpression\n\t\t\t\t\t\t| MultiplicativeExpression\n\t\t\t\t\t\t\n\tstart : OPENTAG statementstates : assignment\n\t\t\t  | postfixExprInc ";"\n\t\t\t  | postfixExprDec ";"\n\t\t\t  | prefixExprInc ";"\n\t\t\t  | prefixExprDec ";"\n\t\t\t  | whileLoop\n\t\t\t  | forEach\n\t\t\t  | return\n\t\t\t  | break\n\t\t\t  | continue\n\t\t\t  | echo \n\t\t\t  | print\n\n\tstatement : states statement\n\t\t\t\t   | end\n\tassignmentOperator : \'=\'\n    | ASS_MUL\n    | ASS_DIV\n    | ASS_MOD\n    | ASS_ADD\n    | ASS_SUB\n    params : args\n\t\t\t  | args \',\' params\n\tassignment : IDENTIFIER assignmentOperator arithmeticExp ";"\n\t\t\t\t\t| IDENTIFIER \'=\' \'[\' params \']\' \';\'\n\t\t\t\t  \n\tpostfixExprInc : IDENTIFIER OP_INC\n\tpostfixExprDec : IDENTIFIER OP_DEC \n\tprefixExprInc : OP_INC IDENTIFIER\n\tprefixExprDec : OP_DEC IDENTIFIER \n\twhileLoop : WHILE \'(\' conditionalExp \')\' \'{\' block \'}\'\n\tforEach : FOREACH \'(\' IDENTIFIER AS IDENTIFIER \')\' \'{\' block \'}\'\n\tconditionalOp : OP_GE\n\t\t\t\t\t | OP_LE\n\t\t\t\t\t | OP_IDENTICAL\n\t\t\t\t\t | OP_NOTIDENTICAL\n\t\t\t\t\t | OP_EQ\n\t\t\t\t\t | OP_NE\n\t\t\t\t\t | \'<\'\n\t\t\t\t\t | \'>\'\n\tconditionalExp : condArgs conditionalOp condArgs\n\t\t\t\t\t  | condArgs\n\t\t\t\t\t  | conditionalExp logicalOp conditionalExp\n\t\t\t\t\t  | \'(\' conditionalExp \')\' logicalOp \'(\' conditionalExp \')\'\n\t\t\t\t\t  | \'(\' conditionalExp \')\' logicalOp conditionalExp\n\t\t\t\t\t  | conditionalExp logicalOp \'(\' conditionalExp \')\'\n\tlogicalOp : OP_LAND\n\t\t\t\t | OP_LOR\n\t\t\t\t | OP_XOR\n\t condArgs : IDENTIFIER\n\t\t\t\t | arithmeticExp\n\t\t\t\t | LNUM_LITERAL\n\t\t\t\t | DNUM_LITERAL\n\tblock : states block\n\t\t\t |\n\treturn : RETURN ";"\n\t\t\t  | RETURN arithmeticExp ";"\n\tbreak : BREAK ";"\n\tcontinue : CONTINUE ";"\n\techo : ECHO ";"\n\t\t\t| ECHO arithmeticExp ";"\n\tprint : PRINT arithmeticExp ";"\n\t\t\t | PRINT \'(\' arithmeticExp \')\' \';\'\n\tend : CLOSETAG'
    
_lr_action_items = {'ASS_MUL':([17,],[53,]),'RETURN':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[10,-31,10,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,10,-44,10,-49,10,-50,]),'OP_LAND':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,86,87,89,90,92,93,94,98,117,119,121,126,131,132,136,138,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,102,-60,-16,-17,-12,-14,-13,102,102,102,-59,102,102,102,102,102,]),'-':([34,35,37,39,40,41,43,44,46,73,74,75,76,83,84,85,89,90,92,93,94,],[67,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-2,-1,-3,-16,-17,-12,-14,-13,]),'OP_IDENTICAL':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,106,-16,-17,-12,-14,-13,]),'OP_INC':([2,5,6,9,10,16,17,18,19,20,22,23,24,27,29,30,38,46,48,49,50,51,52,53,54,55,58,59,60,62,63,64,66,67,68,70,71,72,77,79,80,82,84,95,99,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,124,125,127,130,134,135,139,],[7,-31,7,42,42,-32,56,-26,-28,-21,42,-29,-27,-30,-23,-24,42,75,-74,-22,-25,-77,-37,-36,-38,42,-40,-39,-35,-78,42,-76,42,42,-80,42,42,42,-75,42,-79,42,75,-43,42,-66,-65,-67,-56,-54,-53,-57,42,-55,-52,-51,-58,-81,42,42,7,-44,42,7,42,-49,7,-50,]),'OP_DEC':([2,5,6,9,10,16,17,18,19,20,22,23,24,27,29,30,38,46,48,49,50,51,52,53,54,55,58,59,60,62,63,64,66,67,68,70,71,72,77,79,80,82,84,95,99,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,124,125,127,130,134,135,139,],[8,-31,8,45,45,-32,57,-26,-28,-21,45,-29,-27,-30,-23,-24,45,76,-74,-22,-25,-77,-37,-36,-38,45,-40,-39,-35,-78,45,-76,45,45,-80,45,45,45,-75,45,-79,45,76,-43,45,-66,-65,-67,-56,-54,-53,-57,45,-55,-52,-51,-58,-81,45,45,8,-44,45,8,45,-49,8,-50,]),'PRINT':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[9,-31,9,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,9,-44,9,-49,9,-50,]),'OP_LE':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,110,-16,-17,-12,-14,-13,]),'ASS_DIV':([17,],[52,]),'OP_NE':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,104,-16,-17,-12,-14,-13,]),'%':([35,37,39,40,41,43,44,46,73,74,75,76,83,84,85,89,90,92,93,94,],[-4,-5,-11,-3,71,-6,-2,-1,-9,-10,-7,-8,-2,-1,-3,71,71,-12,-14,-13,]),')':([34,35,37,39,40,41,43,44,46,69,73,74,75,76,81,83,84,85,86,87,89,90,92,93,94,98,119,121,122,126,131,132,136,138,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,91,-9,-10,-7,-8,-69,-2,-1,-3,100,-60,-16,-17,-12,-14,-13,117,-61,-59,129,132,-63,-64,138,-62,]),'(':([9,25,28,63,82,99,101,102,103,118,125,130,],[38,63,65,82,82,118,-66,-65,-67,82,130,82,]),'+':([34,35,37,39,40,41,43,44,46,73,74,75,76,83,84,85,89,90,92,93,94,],[66,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-2,-1,-3,-16,-17,-12,-14,-13,]),'*':([35,37,39,40,41,43,44,46,73,74,75,76,83,84,85,89,90,92,93,94,],[-4,-5,-11,-3,70,-6,-2,-1,-9,-10,-7,-8,-2,-1,-3,70,70,-12,-14,-13,]),'CLOSETAG':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,124,134,139,],[13,-31,13,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,-44,-49,-50,]),'OP_LOR':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,86,87,89,90,92,93,94,98,117,119,121,126,131,132,136,138,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,101,-60,-16,-17,-12,-14,-13,101,101,101,-59,101,101,101,101,101,]),'/':([35,37,39,40,41,43,44,46,73,74,75,76,83,84,85,89,90,92,93,94,],[-4,-5,-11,-3,72,-6,-2,-1,-9,-10,-7,-8,-2,-1,-3,72,72,-12,-14,-13,]),'LNUM_LITERAL':([9,10,22,38,52,53,54,55,58,59,60,63,66,67,70,71,72,79,82,99,101,102,103,104,105,106,107,108,109,110,111,112,115,118,125,130,],[44,44,44,44,-37,-36,-38,44,-40,-39,-35,83,44,44,44,44,44,44,83,83,-66,-65,-67,-56,-54,-53,-57,83,-55,-52,-51,-58,44,83,83,83,]),'BOOL_LITERAL':([9,10,22,38,52,53,54,55,58,59,60,63,66,67,70,71,72,79,82,99,101,102,103,104,105,106,107,108,109,110,111,112,115,118,125,130,],[43,43,43,43,-37,-36,-38,43,-40,-39,-35,43,43,43,43,43,43,43,43,43,-66,-65,-67,-56,-54,-53,-57,43,-55,-52,-51,-58,43,43,43,43,]),';':([3,4,10,11,12,14,22,26,32,33,34,35,36,37,39,40,41,43,44,46,47,56,57,61,73,74,75,76,78,89,90,91,92,93,94,116,],[29,30,48,49,50,51,62,64,-47,-48,-18,-4,68,-5,-11,-3,-15,-6,-2,-1,77,-45,-46,80,-9,-10,-7,-8,95,-16,-17,114,-12,-14,-13,124,]),'IDENTIFIER':([2,5,6,7,8,9,10,16,18,19,20,22,23,24,27,29,30,38,42,45,48,49,50,51,52,53,54,55,58,59,60,62,63,64,65,66,67,68,70,71,72,77,79,80,82,95,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,120,124,125,127,130,134,135,139,],[17,-31,17,32,33,46,46,-32,-26,-28,-21,46,-29,-27,-30,-23,-24,46,73,74,-74,-22,-25,-77,-37,-36,-38,46,-40,-39,-35,-78,84,-76,88,46,46,-80,46,46,46,-75,46,-79,84,-43,84,-66,-65,-67,-56,-54,-53,-57,84,-55,-52,-51,-58,122,-81,46,84,17,-44,84,17,84,-49,17,-50,]),'=':([17,],[60,]),'<':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,107,-16,-17,-12,-14,-13,]),'OPENTAG':([0,],[2,]),'DOUBLE_STRING':([9,10,22,38,52,53,54,55,58,59,60,63,66,67,70,71,72,79,82,99,101,102,103,104,105,106,107,108,109,110,111,112,115,118,125,130,],[37,37,37,37,-37,-36,-38,37,-40,-39,-35,37,37,37,37,37,37,37,37,37,-66,-65,-67,-56,-54,-53,-57,37,-55,-52,-51,-58,37,37,37,37,]),'OP_NOTIDENTICAL':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,105,-16,-17,-12,-14,-13,]),'ASS_ADD':([17,],[59,]),'ASS_MOD':([17,],[54,]),'DNUM_LITERAL':([9,10,22,38,52,53,54,55,58,59,60,63,66,67,70,71,72,79,82,99,101,102,103,104,105,106,107,108,109,110,111,112,115,118,125,130,],[40,40,40,40,-37,-36,-38,40,-40,-39,-35,85,40,40,40,40,40,40,85,85,-66,-65,-67,-56,-54,-53,-57,85,-55,-52,-51,-58,40,85,85,85,]),'ECHO':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[22,-31,22,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,22,-44,22,-49,22,-50,]),'>':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,112,-16,-17,-12,-14,-13,]),'AS':([88,],[113,]),'FOREACH':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[28,-31,28,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,28,-44,28,-49,28,-50,]),'ASS_SUB':([17,],[58,]),'OP_XOR':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,86,87,89,90,92,93,94,98,117,119,121,126,131,132,136,138,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,103,-60,-16,-17,-12,-14,-13,103,103,103,-59,103,103,103,103,103,]),'[':([60,],[79,]),']':([35,37,40,43,44,46,73,74,75,76,96,97,123,],[-4,-5,-3,-6,-2,-1,-9,-10,-7,-8,-41,116,-42,]),',':([35,37,40,43,44,46,73,74,75,76,96,],[-4,-5,-3,-6,-2,-1,-9,-10,-7,-8,115,]),'SINGLE_STRING':([9,10,22,38,52,53,54,55,58,59,60,63,66,67,70,71,72,79,82,99,101,102,103,104,105,106,107,108,109,110,111,112,115,118,125,130,],[35,35,35,35,-37,-36,-38,35,-40,-39,-35,35,35,35,35,35,35,35,35,35,-66,-65,-67,-56,-54,-53,-57,35,-55,-52,-51,-58,35,35,35,35,]),'OP_EQ':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,109,-16,-17,-12,-14,-13,]),'WHILE':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[25,-31,25,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,25,-44,25,-49,25,-50,]),'BREAK':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[26,-31,26,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,26,-44,26,-49,26,-50,]),'CONTINUE':([2,5,6,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,134,135,139,],[14,-31,14,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,14,-44,14,-49,14,-50,]),'{':([100,129,],[120,135,]),'$end':([1,13,15,21,31,],[0,-82,-20,-34,-33,]),'}':([5,16,18,19,20,23,24,27,29,30,48,49,50,51,62,64,68,77,80,95,114,120,124,127,128,133,134,135,137,139,],[-31,-32,-26,-28,-21,-29,-27,-30,-23,-24,-74,-22,-25,-77,-78,-76,-80,-75,-79,-43,-81,-73,-44,-73,134,-72,-49,-73,139,-50,]),'OP_GE':([34,35,37,39,40,41,43,44,46,73,74,75,76,81,83,84,85,87,89,90,92,93,94,],[-18,-4,-5,-11,-3,-15,-6,-2,-1,-9,-10,-7,-8,-69,-2,-1,-3,111,-16,-17,-12,-14,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'postfixExprDec':([2,6,120,127,135,],[3,3,3,3,3,]),'prefixExprInc':([2,6,120,127,135,],[4,4,4,4,4,]),'echo':([2,6,120,127,135,],[5,5,5,5,5,]),'states':([2,6,120,127,135,],[6,6,127,127,127,]),'postfixExprInc':([2,6,120,127,135,],[11,11,11,11,11,]),'arithmeticExp':([9,10,22,38,55,63,82,99,108,118,125,130,],[36,47,61,69,78,81,81,81,81,81,81,81,]),'prefixExprDec':([2,6,120,127,135,],[12,12,12,12,12,]),'MultiplicativeExpression':([9,10,22,38,55,63,66,67,82,99,108,118,125,130,],[41,41,41,41,41,41,89,90,41,41,41,41,41,41,]),'start':([0,],[1,]),'params':([79,115,],[97,123,]),'statement':([2,6,],[15,31,]),'assignmentOperator':([17,],[55,]),'print':([2,6,120,127,135,],[16,16,16,16,16,]),'whileLoop':([2,6,120,127,135,],[18,18,18,18,18,]),'return':([2,6,120,127,135,],[19,19,19,19,19,]),'logicalOp':([86,98,117,119,126,131,132,136,138,],[99,99,125,99,99,99,125,99,125,]),'assignment':([2,6,120,127,135,],[20,20,20,20,20,]),'args':([9,10,22,38,55,63,66,67,70,71,72,79,82,99,108,115,118,125,130,],[39,39,39,39,39,39,39,39,92,93,94,96,39,39,39,96,39,39,39,]),'break':([2,6,120,127,135,],[23,23,23,23,23,]),'forEach':([2,6,120,127,135,],[24,24,24,24,24,]),'end':([2,6,],[21,21,]),'conditionalExp':([63,82,99,118,125,130,],[86,98,119,126,131,136,]),'AdditiveExpression':([9,10,22,38,55,63,82,99,108,118,125,130,],[34,34,34,34,34,34,34,34,34,34,34,34,]),'conditionalOp':([87,],[108,]),'continue':([2,6,120,127,135,],[27,27,27,27,27,]),'condArgs':([63,82,99,108,118,125,130,],[87,87,87,121,87,87,87,]),'block':([120,127,135,],[128,133,137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('args -> IDENTIFIER','args',1,'p_args','php_yacc.py',81),
  ('args -> LNUM_LITERAL','args',1,'p_args','php_yacc.py',82),
  ('args -> DNUM_LITERAL','args',1,'p_args','php_yacc.py',83),
  ('args -> SINGLE_STRING','args',1,'p_args','php_yacc.py',84),
  ('args -> DOUBLE_STRING','args',1,'p_args','php_yacc.py',85),
  ('args -> BOOL_LITERAL','args',1,'p_args','php_yacc.py',86),
  ('args -> IDENTIFIER OP_INC','args',2,'p_args','php_yacc.py',87),
  ('args -> IDENTIFIER OP_DEC','args',2,'p_args','php_yacc.py',88),
  ('args -> OP_INC IDENTIFIER','args',2,'p_args','php_yacc.py',89),
  ('args -> OP_DEC IDENTIFIER','args',2,'p_args','php_yacc.py',90),
  ('MultiplicativeExpression -> args','MultiplicativeExpression',1,'p_MultiplicativeExpression','php_yacc.py',102),
  ('MultiplicativeExpression -> MultiplicativeExpression * args','MultiplicativeExpression',3,'p_MultiplicativeExpression','php_yacc.py',103),
  ('MultiplicativeExpression -> MultiplicativeExpression / args','MultiplicativeExpression',3,'p_MultiplicativeExpression','php_yacc.py',104),
  ('MultiplicativeExpression -> MultiplicativeExpression % args','MultiplicativeExpression',3,'p_MultiplicativeExpression','php_yacc.py',105),
  ('AdditiveExpression -> MultiplicativeExpression','AdditiveExpression',1,'p_AdditiveExpression','php_yacc.py',150),
  ('AdditiveExpression -> AdditiveExpression + MultiplicativeExpression','AdditiveExpression',3,'p_AdditiveExpression','php_yacc.py',151),
  ('AdditiveExpression -> AdditiveExpression - MultiplicativeExpression','AdditiveExpression',3,'p_AdditiveExpression','php_yacc.py',152),
  ('arithmeticExp -> AdditiveExpression','arithmeticExp',1,'p_arithmeticExp','php_yacc.py',198),
  ('arithmeticExp -> MultiplicativeExpression','arithmeticExp',1,'p_arithmeticExp','php_yacc.py',199),
  ('start -> OPENTAG statement','start',2,'p_start','php_yacc.py',206),
  ('states -> assignment','states',1,'p_states','php_yacc.py',212),
  ('states -> postfixExprInc ;','states',2,'p_states','php_yacc.py',213),
  ('states -> postfixExprDec ;','states',2,'p_states','php_yacc.py',214),
  ('states -> prefixExprInc ;','states',2,'p_states','php_yacc.py',215),
  ('states -> prefixExprDec ;','states',2,'p_states','php_yacc.py',216),
  ('states -> whileLoop','states',1,'p_states','php_yacc.py',217),
  ('states -> forEach','states',1,'p_states','php_yacc.py',218),
  ('states -> return','states',1,'p_states','php_yacc.py',219),
  ('states -> break','states',1,'p_states','php_yacc.py',220),
  ('states -> continue','states',1,'p_states','php_yacc.py',221),
  ('states -> echo','states',1,'p_states','php_yacc.py',222),
  ('states -> print','states',1,'p_states','php_yacc.py',223),
  ('statement -> states statement','statement',2,'p_statement','php_yacc.py',234),
  ('statement -> end','statement',1,'p_statement','php_yacc.py',235),
  ('assignmentOperator -> =','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',243),
  ('assignmentOperator -> ASS_MUL','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',244),
  ('assignmentOperator -> ASS_DIV','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',245),
  ('assignmentOperator -> ASS_MOD','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',246),
  ('assignmentOperator -> ASS_ADD','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',247),
  ('assignmentOperator -> ASS_SUB','assignmentOperator',1,'p_assignmentOperator','php_yacc.py',248),
  ('params -> args','params',1,'p_params','php_yacc.py',254),
  ('params -> args , params','params',3,'p_params','php_yacc.py',255),
  ('assignment -> IDENTIFIER assignmentOperator arithmeticExp ;','assignment',4,'p_assignment','php_yacc.py',269),
  ('assignment -> IDENTIFIER = [ params ] ;','assignment',6,'p_assignment','php_yacc.py',270),
  ('postfixExprInc -> IDENTIFIER OP_INC','postfixExprInc',2,'p_postfixExprInc','php_yacc.py',331),
  ('postfixExprDec -> IDENTIFIER OP_DEC','postfixExprDec',2,'p_postfixExprDec','php_yacc.py',349),
  ('prefixExprInc -> OP_INC IDENTIFIER','prefixExprInc',2,'p_prefixExprInc','php_yacc.py',364),
  ('prefixExprDec -> OP_DEC IDENTIFIER','prefixExprDec',2,'p_prefixExprDec','php_yacc.py',379),
  ('whileLoop -> WHILE ( conditionalExp ) { block }','whileLoop',7,'p_whileLoop','php_yacc.py',394),
  ('forEach -> FOREACH ( IDENTIFIER AS IDENTIFIER ) { block }','forEach',9,'p_forEach','php_yacc.py',405),
  ('conditionalOp -> OP_GE','conditionalOp',1,'p_conditionalOp','php_yacc.py',412),
  ('conditionalOp -> OP_LE','conditionalOp',1,'p_conditionalOp','php_yacc.py',413),
  ('conditionalOp -> OP_IDENTICAL','conditionalOp',1,'p_conditionalOp','php_yacc.py',414),
  ('conditionalOp -> OP_NOTIDENTICAL','conditionalOp',1,'p_conditionalOp','php_yacc.py',415),
  ('conditionalOp -> OP_EQ','conditionalOp',1,'p_conditionalOp','php_yacc.py',416),
  ('conditionalOp -> OP_NE','conditionalOp',1,'p_conditionalOp','php_yacc.py',417),
  ('conditionalOp -> <','conditionalOp',1,'p_conditionalOp','php_yacc.py',418),
  ('conditionalOp -> >','conditionalOp',1,'p_conditionalOp','php_yacc.py',419),
  ('conditionalExp -> condArgs conditionalOp condArgs','conditionalExp',3,'p_conditionalExp','php_yacc.py',424),
  ('conditionalExp -> condArgs','conditionalExp',1,'p_conditionalExp','php_yacc.py',425),
  ('conditionalExp -> conditionalExp logicalOp conditionalExp','conditionalExp',3,'p_conditionalExp','php_yacc.py',426),
  ('conditionalExp -> ( conditionalExp ) logicalOp ( conditionalExp )','conditionalExp',7,'p_conditionalExp','php_yacc.py',427),
  ('conditionalExp -> ( conditionalExp ) logicalOp conditionalExp','conditionalExp',5,'p_conditionalExp','php_yacc.py',428),
  ('conditionalExp -> conditionalExp logicalOp ( conditionalExp )','conditionalExp',5,'p_conditionalExp','php_yacc.py',429),
  ('logicalOp -> OP_LAND','logicalOp',1,'p_logicalOp','php_yacc.py',481),
  ('logicalOp -> OP_LOR','logicalOp',1,'p_logicalOp','php_yacc.py',482),
  ('logicalOp -> OP_XOR','logicalOp',1,'p_logicalOp','php_yacc.py',483),
  ('condArgs -> IDENTIFIER','condArgs',1,'p_condArgs','php_yacc.py',488),
  ('condArgs -> arithmeticExp','condArgs',1,'p_condArgs','php_yacc.py',489),
  ('condArgs -> LNUM_LITERAL','condArgs',1,'p_condArgs','php_yacc.py',490),
  ('condArgs -> DNUM_LITERAL','condArgs',1,'p_condArgs','php_yacc.py',491),
  ('block -> states block','block',2,'p_block','php_yacc.py',503),
  ('block -> <empty>','block',0,'p_block','php_yacc.py',504),
  ('return -> RETURN ;','return',2,'p_return','php_yacc.py',512),
  ('return -> RETURN arithmeticExp ;','return',3,'p_return','php_yacc.py',513),
  ('break -> BREAK ;','break',2,'p_break','php_yacc.py',525),
  ('continue -> CONTINUE ;','continue',2,'p_continue','php_yacc.py',531),
  ('echo -> ECHO ;','echo',2,'p_echo','php_yacc.py',537),
  ('echo -> ECHO arithmeticExp ;','echo',3,'p_echo','php_yacc.py',538),
  ('print -> PRINT arithmeticExp ;','print',3,'p_print','php_yacc.py',550),
  ('print -> PRINT ( arithmeticExp ) ;','print',5,'p_print','php_yacc.py',551),
  ('end -> CLOSETAG','end',1,'p_end','php_yacc.py',559),
]
