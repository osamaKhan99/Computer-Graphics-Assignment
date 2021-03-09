from pyDatalog import pyDatalog


pyDatalog.create_terms("Factorial, N")
Factorial[N] = N*Factorial[N-1]
Factorial[1] = 1
print( Factorial[7] == N,'\n')

pyDatalog.create_terms('parent,bill,marry,john,ancestor,X,Y,Z')
+parent(bill,marry)
+parent(marry,john)
ancestor(X,Y) <= parent(X,Y)
ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)
print(ancestor(bill,X))
