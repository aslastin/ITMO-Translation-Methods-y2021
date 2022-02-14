grammar Sas;
@parser::members {
    self._is_outside = True
    self._is_in_func = False
    self._cnt = 0

def inUnit(self):
    self._is_outside = False
    self._cnt += 1

def outUnit(self):
    self._cnt -= 1
    if self._cnt == 0:
        self._is_outside = True

def inFunc(self):
    self._is_in_func = True
    self._is_outside = False

def outFunc(self):
    self._is_in_func = False
    self._is_outside = True
}

prog : stat* ;

stat : {self._is_outside}? {self.inFunc()} func {self.outFunc()}   # StatFunc
     | {self._is_in_func}? 'r@' expr ';'                           # StatReturn
     | {self.inUnit()} unitWithBody {self.outUnit()}               # StatUnitWithBody
     | const='cnst@'? varList '=' exprList ';'                     # StatAssign
     | expr ';'                                                    # StatExpr
     ;

func : 'f@' ID '(' varList? ')' '{' prog '}' ;

exprBase : f '(' exprList? ')'                              # ExprFuncCall
          | '(' expr ')'                                    # ExprBrackets
          | '|' exprBase '|'                                # ExprAbs
          | <assoc=right> e1=exprBase '^' e2=exprBase       # ExprPow
          | op=('+'|'-') exprBase                           # ExprUnary
          | e1=exprBase op=('*'|'/'|'%') e2=exprBase        # ExprMult
          | e1=exprBase op=('+'|'-') e2=exprBase            # ExprAdd
          | boolean                                         # ExprBool
          | var                                             # ExprVar
          | number                                          # ExprNumber
          ;

expr : exprBase                                                                                  # ExprBaseCall
     | exprBase rightCmp+                                                                         # ExprCmp
     | exprBase ('==' exprBase)+                                                                 # ExprEq
     | e1=exprBase '!=' e2=exprBase                                                              # ExprNeq
     | e1=expr 'and' e2=expr                                                                     # ExprAnd
     | e1=expr 'xor' e2=expr                                                                     # ExprXor
     | e1=expr 'or' e2=expr                                                                      # ExprOr
     ;

rightCmp : opCmp exprBase ;

opCmp : '<'|'<='|'>'|'>=' ;

unitWithBody : if_      # UnitIf
             | for_     # UnitFor
             | while_   # UnitWhile
             ;

varList : var (',' var)* ;

var : ID ;

exprList : expr (',' expr)* ;

number : DOUBLE
       | LONG
       | INT
       ;

boolean : 'true' | 'false' ;

f : ID t?;

t : '<' ID '>';

if_ : 'if@' '(' expr ')' '{' prog '}'               # If
    | 'ifelse@' '(' expr ')' '{' prog '|' prog '}'  # IfElse
    ;

for_ : 'for@' '(' forSeq (',' forStat)* ')' '{' prog '}' ;

forStat : forSeq  # ForStatSeq
        | expr    # ForStatExpr
        ;

forSeq : var '<-' seq ;
seq : '[' start=expr (',' follow=expr)? '..' end=expr lb=(']'|')') ;


while_ : 'while@' '(' expr ')' '{' prog '}' ;

ID : LETTER (LETTER | DIGIT)* ;
fragment LETTER: [a-zA-Z] ;
fragment DIGIT: [0-9] ;

DOUBLE : INT_DIGITS '.' INT_DIGITS EXP?
       | INT_DIGITS EXP
       ;

LONG : INT_DIGITS 'L' ;

INT : INT_DIGITS ;

fragment INT_DIGITS : '0' | '1'..'9' '0'..'9'* ;
fragment EXP : [Ee] [+\-]? INT_DIGITS ;

LINE_COMMENT : '//' .*? '\n' -> skip ;
COMMENT : '/*' .*? '*/' -> skip ;

WS: [ \t\r\n] -> skip;
