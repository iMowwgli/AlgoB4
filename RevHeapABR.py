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

def average_balances(B):
    if B == None:
        return 0
    else:
        totbal = total_balances(B)
        totnode = total_nodes(B)
        return totbal / totnode
    
def total_balances(B):
    if B == None:
        return 0
    else:
        bal_l = total_balances(B.left)
        bal_r = total_balances(B.right)
        return B.left.bal + B.right.bal + bal_l + bal_r
    
def total_nodes(B):
    if B == None:
        return 0
    else:
        node_l = total_nodes(B.left)
        node_r = total_nodes(B.right)
        return 1 + node_l + node_r

