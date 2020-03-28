#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"
c =Tree('-',None,Tree('p',None,None))
#print(Inorder(c))

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    return pila[-1]

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def complemento(l):
    if len(l) == 2:
        return l[1]
    elif len(l) == 1:
        return '-' + str(l) 


def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False 
    h=l;
    for x in range(0, len(h)):
        i = h[x]
        n = complemento(i)
        for c in range(x+1, len(h)):
            k = h[c]
            if k == n:
                return True
            
    return False
#print(par_complementario( ['p', 'q','-p','-q']))

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False

    h = Inorder(f)

    if len(h) == 2 or len(h) == 1:
        return True
    
    return False

#c = [Tree('y',Tree('r',None, None), Tree('q',None, None)),Tree('q',None,None), Tree('-',None,Tree('p',None,None)),Tree('-', None,Tree('-', None, Tree('r',None,None)))]
#for t in range(0, len(c)):
#    j = c[t]
#    print(es_literal(j))

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
#    cadena = []
#    for i in range(0, len(l)):
#        h = l[i]
#        f = Inorder(h)
#        cadena.appent(f)
    #f = []
    for x in range(0, len(l)):
        p = l[x]
        if es_literal(p) == False:
            return False
#        else:
#            f.appent(p)
    return None
c = [Tree('q',None,None), Tree('-', None, Tree('r', None, None))]
print(no_literales(c))

def clasifica(f):
    if f.label == '-':
        if f.right.label == '-':
            return '1alfa'
        elif f.right.label == 'O':
            return '3alfa'
        elif f.right.label == 'Y':
            return '1beta'
        elif f.right.label == '>':
            return '4alfa'
    elif f.label =='Y':
        return '2alfa'
    elif f.label == 'O':
        return '2beta'
    elif f.label == '>':
        return '3beta'

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas

    h = clasifica(f)
    if h == '1alfa':
        listaHojas.append(Inorder(f.right.right))
    if h == '2alfa':
        listaHojas.append(Inorder(f.right), Inorder(f.left))
    if h == '3alfa':
        listaHojas.append('-'+ Inorder(f.right.left),'-' + Inorder(f.right.right))
	#global listaHojas
c = Tree('-', None, Tree('-', None, Tree('p', None, None)))
h = Tree('Y',Tree('p', None, None), ('r', None, None))
print(clasifica_y_extiende(h))
def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = StringtoTree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
