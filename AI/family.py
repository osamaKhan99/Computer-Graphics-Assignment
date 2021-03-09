# Q2. Now using the above program create your family database ‘family.py’ and store in it
# the facts about your family using predicates ‘mother’, ’married’, ’male’ and ‘female’

#  mother(X,Y) is true if the mother of X is Y
#  married(X,Y) is true if the husband of X is Y
#  male(X) is true is X is male
#  female(X) is true if X is female

from pyDatalog import pyDatalog

pyDatalog.create_terms("mother,married,male,female,husband,Ali,Uzair,Ayesha,X,Y")

+male('Ali')
+male('Uzair')
+female('Ayesha')
+mother('Ayesha', 'Ali')
+husband('Uzair', 'Ayesha')

mother(X,Y) <= mother(X,Y)
married(X,Y) <= husband(Y,X)
male(X) <= male(X)
female(X) <= female(X)
print(mother(X,'Ali'),'\n')

pyDatalog.create_terms("Male, Female, grandfather, grandmother, parent, father, mother, aunt, sister, brother, Father_Name, Son1, Son2, Daughter1, Daughter2, Mother_Name, X, Y, Z")
+Male("Father_Name")
+Male("Son1")
+Male("Son2")
+Female("Daughter1")
+Female("Daughter2")
+Female("Mother_Name")

+parent("Father_Name", "Son1")
+parent("Father_Name", "Son2")
+parent("Father_Name", "Daughter1")
+parent("Father_Name", "Daughter2")
+parent("Mother_Name", "Son1")
+parent("Mother_Name", "Son2")
+parent("Mother_Name", "Daughter1")
+parent("Mother_Name", "Daughter2")

#Defining rules.
father(X,Y) <= Male(X) , parent(X,Y)
mother(X,Y) <= Female(X) , parent(X,Y)
grandfather(X,Z) <= Male(X) & parent(X,Y) & parent(Y,Z)
grandmother(X,Z) <= Female(X) & parent(X,Y) & parent(Y,Z)
aunt(X,Z) <= Female(X) & sister(X,Y) & mother(Y,Z)
print( father(X,"Son1") )
print('\n')
print( mother(X,"Daughter2") )