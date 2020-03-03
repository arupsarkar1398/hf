#This is a program to calculate the Hartree-Fock energy of a closed shell moleecule
from no_of_electron import no_of_e
from distance import find_distance
from file_read import file_read
import numpy as np

#Read the geometry
input_file=open('geom.dat') #open the file

file_content=input_file.readlines()  #read the content in list format

input_file.close()    #close the file

#print(file_content)


#store the input in list
temp_geom=[]
for line in file_content:
    v_line=line.rstrip()
    if len(v_line)>0:
         temp_geom.append(v_line.split())

print(temp_geom)


#no of atoms

NATOM=int(temp_geom[0][0])

print('Total no of atoms '+str(NATOM))
ATOM_SYMBOL=[] #this list contains the atom symbols
GEOM=[] #cartesian coordinate

for i in range(1,NATOM+1):
    ATOM_SYMBOL.append(temp_geom[i][0])
    GEOM.append(temp_geom[i][1:4])
print('Atom Symbol')
print(ATOM_SYMBOL)

print('Cartesian Coordinate in a.u.')
print(GEOM)

#count the total number of electrons
NE=0 #this is the total no of electron

for i in range(len(ATOM_SYMBOL)):
    k=no_of_e(ATOM_SYMBOL[i])
    NE+=k
print('Total no of electron is '+str(NE))

#calculate the nuclear repulsion energy 
E_nuc=0.0
for i in range (NATOM):
    for j in range(0,i):
        Z_a=no_of_e(ATOM_SYMBOL[i])
        Z_b=no_of_e(ATOM_SYMBOL[j])
        R_ab=find_distance(GEOM[i],GEOM[j])
        print(R_ab)
        E_nuc+=(Z_a*Z_b)/R_ab
print('Nuclear repulsion energy '+str(E_nuc)+ ' a.u.')

#reading files
#basis set dimension
nbasis=7

S=file_read('s.dat' ,nbasis)

V=file_read('v.dat' ,nbasis)
T=file_read('t.dat' ,nbasis)

#hcore
H_core=np.zeros([nbasis,nbasis])
H_core=np.add(V,T)
print(H_core)

#read one electron integrals
#read s

#S=read_file('s.dat',nbasis)

#twoe=read_2_e(nbasis)
#print(twoe)







    
