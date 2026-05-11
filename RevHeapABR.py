from collections import deque
# -*- coding: utf-8 -*-
"""Binary Tree module"""

class BinTree:
    """Simple class for binary tree

    Attributes:
        key (Any): Node key.
        left (BinTree): Left child.
        right (BinTree): Right child.

    """

    def __init__(self, key, left, right):
        """Init binary tree.

        Args:
            key (Any): Node key.
            left (BinTree): Left child.
            right (BinTree): Right child.

        """

        self.key = key
        self.left = left
        self.right = right

# -*- coding: utf-8 -*-
"""Queue module.
    All operations are in constant time
"""

class Queue:
    """Simple class for FIFO (first-in-first-out) container."""

    def __init__(self):
        """Init queue."""

        self.elements = deque()

    def enqueue(self, elt):
        """Add an element to the queue.

        Args:
            elt (Any): Element to enqueue.

        """

        self.elements.append(elt)

    def dequeue(self):
        """Remove and return next element from the queue.

        Returns:
            Any: Element from the queue.

        Raises:
            IndexError: If queue is empty.

        """

        return self.elements.popleft()

    def isempty(self):
        """Check whether queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.

        """

        return len(self.elements) == 0
    

    # -*- coding: utf-8 -*-

"""
AVL Module
"""

class AVL:
    """AVL main class."""
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal

def to_str(B, s=""):
    """
    Simple AVL to String conversion for "print"
    Warning : B is not empty! (not optimized...)
    """
    r = s + '- ' + str(B.key) + ' (' + str(B.bal) + ')\n'
    if B.left != None or B.right != None: # internal node
        if B.left!= None:
            r += to_str(B.left, s + "  |")
        else:
            r += s + "  |" + '- '+ '\n'
        if B.right != None:
            r += to_str(B.right, s + "  |")
        else:
            r += s + "  |" + '- '+ '\n'
    return r



"""----------------------------------------------------------------------------------------------------------------------------------------------"""


def search(B,x):
    if x == B.key:
        return B
    if x > B.key:
        return search(B.right,x)
    elif x < B.key:
        return search(B.left,x)
    else:
        return None
    

def counteven(B):
    if B == None:
        return 0
    else:
        count_l = counteven(B.left)
        count_r = counteven(B.right)

        if (B.key % 2 == 0):
            return count_r + count_l + 1
        else:
            return count_l + count_r
        
        
def sumkeyeven(B):
    if B == None:
        return 0
    else:
        count_l = sumkeyeven(B.left)
        count_r = sumkeyeven(B.right)

        if (B.key % 2 == 0):
            return B.key + count_l + count_r
        else:
            return count_l + count_r

        
# qui retourne le nombre de clés dans l'intervalle [a, b] en utilisant l'élagage pour être optimal. 
def count_interval(B, a, b):
    if B == None:
        return 0
    
    if B.key < a:
        # Élagage : tout le côté gauche est forcément < a, on l'ignore
        return count_interval(B.right, a, b) 
        
    elif B.key > b:
        # Élagage : tout le côté droit est forcément > b, on l'ignore
        return count_interval(B.left, a, b) 
        
    else:
        # La clé est dans [a, b]
        # On additionne : le nœud actuel (1) + gauche + droite
        res_g = count_interval(B.left, a, b) 
        res_d = count_interval(B.right, a, b)
        return 1 + res_g + res_d
            
def delete_smaller(B, x):
    if B == None:
        return None
    else:
        if B.key < x:
            return delete_smaller(B.right,x)
        else:
            B.left = delete_smaller(B.left,x)
    return B
    
def are_mirrors(B1, B2):
    if B1 == None:
        return B2 == None
    if B2 == None:
        return False
    
    if B1.key == B2.key:
        if are_mirrors(B1.left,B2.right):
            return are_mirrors(B1.right,B2.left)

def symmetric(B):
    if B == None:
        return True
    else:
        return are_mirrors(B.left,B.right)
    
def leaf_insert(B, x):
    # Règle 2 : Cas de base B == None en PREMIER
    if B == None:
        # On crée le nœud et on renvoie True (insertion réussie)
        return (BinTree(x, None, None),True)
    # Gestion des doublons (demandé dans l'énoncé)
    if B.key == x:
        return (B, False)
    # Règle 3 : Élagage / Invariant BST 
    if x < B.key:
        # Règle 1 : L'appelant affecte B.left = f(B.left)
        (B.left,inserted) = leaf_insert(B.left, x)
    else:
        (B.right, inserted) = leaf_insert(B.right, x)
    # On retourne toujours l'arbre (B) et l'info demandée
    return (B, inserted)
            
def delete(B,x):
    if B == None:
        return None
    else:
        if B.key < x:
            B.right = delete(B.right,x)
        elif B.key > x:
            B.left = delete(B.left,x)
        else:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                B.key = maxBST(B.left)
                B.left = delete(B.left,B.key)
    return B

def maxBST(B):
    if B.right == None:
        return B.key
    else:
        return maxBST(B.right)


#Écrire la fonction average_balances (B) qui calcule la moyenne des déséquilibres de tous les nœuds
#de l'arbre binaire (class BinTree) B. Si l'arbre est vide la fonction retourne 0.
def total_balances(B):
    """Calcule la somme de toutes les balances présentes dans l'arbre."""
    res = 0
    if B != None:
        # On utilise directement l'attribut .bal existant
        res = B.bal + total_balances(B.left) + total_balances(B.right)
    return res

def total_nodes(B):
    """Compte le nombre total de nœuds de l'arbre."""
    res = 0
    if B != None:
        res = 1 + total_nodes(B.left) + total_nodes(B.right)
    return res

def average_balances(B):
    """Retourne la moyenne des balances, ou 0 si l'arbre est vide."""
    res = 0
    if B != None:
        tot_bal = total_balances(B)
        tot_nodes = total_nodes(B)
        res = tot_bal / tot_nodes
    return res


def heap_push(H, val):
    H.append(val)
    i = len(H) - 1
    # Tant qu'on n'est pas à la racine et que le fils < père
    while i > 1 and H[i] < H[i // 2]:
        H[i], H[i // 2] = H[i // 2], H[i]
        i = i // 2

def heap_pop(H):
    if len(H) <= 1:
        return None
    res = H[1]
    H[1] = H[-1]
    H.pop()
    n = len(H) - 1
    i = 1
    while 2 * i <= n: # Tant qu'il y a au moins un fils
        j = 2 * i # Fils gauche
        if j < n and H[j+1] < H[j]: # Si fils droit existe et est plus petit
            j = j + 1
        if H[i] <= H[j]: # Si l'ordre est respecté
            break
        H[i], H[j] = H[j], H[i]
        i = j
    return res


#------------------------------------------------------------------------------
# rotations: works only in "useful" cases

def lr(A): # left rotation
    '''
    A: AVL
    applies a left rotation on A and returns the new root of the AVL
    '''
    aux = A.right 
    A.right = aux.left
    aux.left = A
    aux.bal += 1
    A.bal = -aux.bal
    return aux

def rr(A): # right rotation
    '''
    A: AVL
    applies a right rotation on A and returns the new root of the AVL
    '''
    aux = A.left
    A.left = aux.right
    aux.right = A
    aux.bal -= 1
    A.bal = -aux.bal
    return aux

def lrr(A): # left-right rotation
    '''
    A: AVL
    applies a left-right rotation on A and returns the new root of the AVL
    '''
    # left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
    # right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A

def rlr(A): # right-left rotation
    '''
    A: AVL
    applies a right-left rotation on A and returns the new root of the AVL
    '''
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    
    (aux.left.bal, aux.right.bal) = (0, 0)
    if aux.bal == -1:
        aux.left.bal = 1
    elif aux.bal == 1:
        aux.right.bal = -1
    aux.bal = 0

    return aux

#------------------------------------------------------------------------------
        
'''
insertion
'''

def __insertAVL(A, x):
    '''
    A: AVL
    x: element
    inserts x in the AVL A if it is not already in the AVL
    returns (newA, b) where
    - newA is the potentially new root of the AVL
    - b is True if the height of the AVL A has changed, False otherwise
    '''
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    else:
        if x < A.key:
            (A.left, dh) = __insertAVL(A.left, x)
            if not dh:
                return (A, False)
            else:
                A.bal += 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == 1:
                    return (A, True)
                else: # A.bal == 2
                    if A.left.bal == 1:
#                        print(x, "rr", A.key)
                        A = rr(A)
                    else:
#                        print(x, "lrr", A.key)
                        A = lrr(A)
                    return (A, False)
        else:   # x > A.key
            (A.right, dh) = __insertAVL(A.right, x)
            if not dh:
                return (A, False)
            else:
                A.bal -= 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == -1:
                    return (A, True)
                else:
                    if A.right.bal == -1:
#                        print(x, "lr", A.key)
                        A = lr(A)
                    else:
#                        print(x, "rlr", A.key)
                        A = rlr(A)
                    return (A, False)
                    
            
            
def insertAVL(A, x):
    '''
    A: AVL
    x: element
    inserts x in the AVL A if it is not already in the AVL
    returns the potentially new root of the AVL
    '''
    (A, dh) = __insertAVL(A, x)
    return A
        

def buildAVLfromList(L, A = None):
    for x in L:
        A = insertAVL(A, x)
    return A

'''
deletion
'''

# non optimized

def maxBST(B):
    '''
    B: Non-empty AVL
    returns the maximum element of the AVL B
    '''
    while B.right != None:
        B = B.right
    return B.key
    
def __deleteAVL(A, x):
    '''
    A: AVL
    x: element
    deletes the element x in the AVL A
    returns (newA, b) where
    - newA is the potentially new root of the AVL
    - b is True if the height of the AVL A has changed, False otherwise
    '''
    if A == None:
        return (None, False)
        
    elif x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key   # to use the case <=
        else:
            if A.left == None:
                return(A.right, True)
            else:
                return(A.left, True)
                
    if x <= A.key:      
        (A.left, dh) = __deleteAVL(A.left, x)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1              # long version
            if A.bal == 0:
                return (A, True)
            elif A.bal == -1:
                return (A, False)
            else:   # A.bal == -2
                if A.right.bal == -1:
#                    print("lr", A.key)
                    A = lr(A)
                    return (A, True)
                elif A.right.bal == 0:
#                    print("lr", A.key)
                    A = lr(A)
                    return (A, False)
                else:
#                    print("rlr", A.key)
                    A = rlr(A)
                    return (A, True)
           
    else:   # x > A.key
        (A.right, dh) = __deleteAVL(A.right, x)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == -1:
#                    print("lrr", A.key)
                    A = lrr(A)
                else:
#                    print("rr", A.key)
                    A = rr(A)
            return (A, A.bal == 0)  
                   # this shortcut also works in previous case!

def deleteAVL(A, x):
    '''
    A: AVL
    x: element
    deletes the element x in the AVL A
    returns the potentially new root of A
    '''
    (A, _) = __deleteAVL(A, x)
    return A

def heap_sort(L):
    """ sorts the associative list of (elements, values) L in increasing order according to values (not in place)
    
        :param L: a list containing pairs (element: any, value: int)
        :rtype: (any, num) list (the new list sorted)
    """
    H = [None] # on laisse la position 0 du tas vide pour simplifier les calculs d'indices
    for (v, e) in L: #attention : (v, e) et pas (e, v) pour respecter l'ordre de tri demandé
        heap_push(H, v, e) 
    L = []
    while H != [None]: # tant que le tas n'est pas vide
        (v, e) = heap_pop(H) # on récupère le minimum (v, e) du tas
        L.append((v, e)) # on ajoute ce minimum à la liste résultat
    return L # la liste L est triée à la fin de l'algorithme




def total_balances(B):
    res = 0
    if B != None:
        # On additionne la balance actuelle et les totaux des fils
        res = B.bal + total_balances(B.left) + total_balances(B.right)
    return res


def total_nodes(B):
    res = 0
    if B != None:
        res = 1 + total_nodes(B.left) + total_nodes(B.right)
    return res


def average_balances(B):
    res = 0
    if B != None:
        tot_bal = total_balances(B)
        tot_nodes = total_nodes(B)
        res = tot_bal / tot_nodes
    return res