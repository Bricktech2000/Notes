% https://www.scryer.pl/

:- use_module(library(si)).
:- use_module(library(dif)).
:- use_module(library(dcgs)).
:- use_module(library(reif)).
:- use_module(library(lists)).

:- op(750,yfx,@).

ws --> [].
ws --> " ", ws.

letter(C) --> [C], { char_type(C,alphabetic) }.
digit(D)  --> [D], { char_type(D,decimal_digit) }.

identifier([X,D]) --> digit(D), letter(X).
identifier([X])   -->           letter(X).

atom(X) --> identifier(X).
atom(X) --> ")", appl(X), "(".

appl(X@Y) --> ws, atom(Y), appl(X).
appl(X)   --> ws, atom(X), ws.

parse(S,AST)   :- reverse(S,S_), phrase(appl(AST),S_).
unparse(AST,S) :- phrase(appl(AST),S_), reverse(S,S_).

rewrite(Xs,Xs,[]).
rewrite(Xs,A,[(LHS,RHS)|Elses]) :- if_(Xs=LHS,eval(RHS,A),rewrite(Xs,A,Elses)).

eval1(Xs,A) :- rewrite(Xs,A,
	[ ("M"@X,                   X@X)
	, ("K"@X@_,                 X)
	, ("I"@X,                   X)
	, ("L"@X@Y,                 X@(Y@Y))
	, ("B"@X@Y@Z,               X@(Y@Z))
	, ("D"@X@Y@Z@W,             X@Y@(Z@W))
	, ("B1"@X@Y@Z@W,            X@(Y@Z@W))
	, ("E"@X@Y@Z@W@V,           X@Y@(Z@W@V))
	, ("B2"@X@Y@Z@W@V,          X@(Y@Z@W@V))
	, ("D1"@X@Y@Z@W@V,          X@Y@Z@(W@V))
	, ("B3"@X@Y@Z@W,            X@(Y@(Z@W)))
	, ("D2"@X@Y@Z@W@V,          X@(Y@Z)@(W@V))
	, ("Ê"@X@Y1@Y2@Y3@Z1@Z2@Z3, X@(Y1@Y2@Y3)@(Z1@Z2@Z3))
	, ("W"@X@Y,                 X@Y@Y)
	, ("C"@X@Y@Z,               X@Z@Y)
	, ("T"@X@Y,                 Y@X)
	, ("R"@X@Y@Z,               Y@Z@X)
	, ("S"@X@Y@Z,               X@Z@(Y@Z))
	]).

eval(X,   X) :- list_si(X).
eval(X0@Y,E) :- eval(X0,X1), eval1(X1@Y,E).

eval_strict_(X,   X)    :- list_si(X).
eval_strict_(X@Y0,X@Y1) :- eval_strict(Y0,Y1).
eval_strict --> eval, eval_strict_.

run        --> parse, eval,        unparse.
run_strict --> parse, eval_strict, unparse.
?- run("BBBBBxyzw",Out).
   Out = "x(y(zw))" ;  ... .
?- run("Ia(Ib)",Out).
   Out = "a(Ib)" ;  ... .
?- run_strict("Ia(Ib)",Out).
   Out = "ab" ;  ... .



% 🅱️🅱️
% 🅱️ 🅱️
% 🅱️🅱️
% 🅱️ 🅱️
% 🅱️🅱️

bigb(B,      B)  :- list_si(B).  % x(yz) -> B, xyz -> x
bigb(Bs,     Bs) :- Bs = (_@"B").
bigb(B@C,    Bs) :- list_si(C), dif(C,"B"), bigb(B,Bs).
bigb(B@(C@D),Bs) :- bigb("B"@B@C@D,Bs).
bluebird --> parse, bigb, eval_strict, unparse.  % eval simplifies
?- Target = "x(yz)(ab(cd))", bluebird(Target,S0), append(S0,"xyzabcd",S1), run_strict(S1,Target).
   Target = "x(yz)(ab(cd))", S0 = "BB(B(B(BB(BB))B))", S1 = "BB(B(B(BB(BB))B))xyzabcd" ;  ... .



%--------------------
% bracket abstraction
%--------------------

no_x(X,Y)   :- list_si(Y), dif(X,Y).
no_x(X,A@B) :- no_x(X,A), no_x(X,B).
abstract_(X,X,  "I").
abstract_(X,B,  "K"@B)     :- no_x(X,B).
abstract_(X,B@C,"S"@B_@C_) :- abstract_(X,B,B_), abstract_(X,C,C_).
abstract(Vars) --> { reverse(Vars,Vars_) }, parse, foldl(abstract_,Vars_), unparse.  % eval would never simplify here unless the input could already be simplified
?- Target = "x(yz)", abstract(["x","y","z"],Target,S0), append(S0,"xyz",S1), run_strict(S1,Target).
   Target = "x(yz)", S0 = "S(S(KS)(S(KK)(S(KS)(S(KK)I))))(K(S(S(KS)(S(KK)I))(KI)))", S1 = "S(S(KS)(S(KK)(S(KS)(S(KK)I))))(K(S(S(KS)(S(KK)I))(KI)))xyz"  % the query succeeded and didn't fail, meaning that S1 evaluates to Target
;  ... .
?- abstract(["x","y"],"xyy",S).
   S = "S(S(KS)(S(S(KS)(S(KK)I))(KI)))(KI)"
;  ... .
