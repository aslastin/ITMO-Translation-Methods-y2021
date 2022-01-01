grammar ALR;

start : WS? desc+ WS?;

desc : nterminal '->' rights ';'            # DescRule
     | terminal ':' regexp ';'              # DescTerminal
     | terminal ':' regexp '=>' skip ';'    # DescSkip
     ;

rights : right ('|' right)* ;

right : member+                       # RightMember
      | eps                           # RightEps
      ;

member : nterminal                    # MemberNterminal
       | terminal                     # MemberTerminal
       | regexp                       # MemberRegexp
       | func                         # MemberFunc
       ;

eps : WS? ;

nterminal : WS? NTERMINAL WS? CONSTRUCTOR? WS? ;
terminal :  WS? TERMINAL WS? ;
regexp :    WS? REGEXP WS? ;
func :      WS? FUNC WS? ;

skip: WS? 'skip' WS? ;

NTERMINAL : [A-Z] (LETTER | DIGIT | '_')* ;
TERMINAL : [a-z] (LETTER | DIGIT | '_')* ;

fragment LETTER: [a-zA-Z] ;
fragment DIGIT: [0-9] ;

FUNC :  '{' FUNC_BODY '}' ;
fragment FUNC_BODY : ~('{' | '}')* ;

REGEXP : '"' REGEXP_BODY '"' ;
fragment REGEXP_BODY : ~('\r' | '\n' | '"')* ;

CONSTRUCTOR : '(' FIELD (',' FIELD)* ')' ;
fragment FIELD: ~(',' | ')')+? ;

WS: [ \t\r\n]+ ;
