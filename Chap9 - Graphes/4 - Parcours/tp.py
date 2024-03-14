from ds import Graphe, Pile, File
from random import randint

def arcs_vers_graphe_no(aretes):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    pass

aretes = [(0, 1), (0, 3),
            (0, 6), (1, 4), (1, 6),
            (2, 5), (3, 6), (3, 8),
            (4, 7), (5, 6), (5, 7)]    
g1 = arcs_vers_graphe_no(aretes)
g1.decrire()

aretes = [(0, 1), (0, 5),
    (1, 2), (1, 6), (1, 5), (2, 3),
    (2, 7), (2, 6), (3, 7), (3, 4),
    (4, 5), (4, 6), (4, 7), (5, 6),
    (6, 7)]    
g2 = arcs_vers_graphe_no(aretes)
g2.decrire()

aretes = [(0, 8), (0, 6), (0, 1),
    (0, 2), (0, 7), (1, 2), (1, 6),
    (1, 8), (1, 4), (2, 4), (2, 5),
    (2, 7), (3, 4), (3, 8), (4, 5),
    (4, 7), (5, 7), (6, 8)]    
g3 = arcs_vers_graphe_no(aretes)
g3.decrire()

g4 = Graphe()
aretes = [(0, 1), (0, 2),
    (1, 2), (1, 3), (2, 3), (4, 5)]
g4 = arcs_vers_graphe_no(aretes)
g4.decrire()

def parcours_aleatoire(G, depart, nombre_sauts):
    """ Graphe, Sommet, int -> {Sommet: int}
    Parcourt aléatoirement le graphe G depuis le sommet depart
    en effectuant nombre_sauts choix de sommets. """
    pass

def parcours_largeur(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = []
    à_explorer = ...
    ...
    while ...
        sommet = ...
        if sommet in vus:
            continue
        # opération de traitement
        vus.append(sommet)
        # ajout des voisins non visités
        for destination in G.voisins(sommet):
            if ...:
                ...
    return vus

def frequences(histo):
    """ {Sommet: int} -> {Sommet: float}
    Renvoie le dictionnaire des fréquences (arrondies au centième)
    associé au dictionnaire du nombre d'occurrences des histo du graphe """
    pass

def parcours_profondeur(G, depart, vus):
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcourt le graphe G depuis depart en profondeur (sachant que
    la liste des sommets présents dans vus ont déjà été visités).
    On suppose que depart n'est pas dans vus. """
    vus.append(depart)
    # appels récursif sur les voisins non visités
    for destination in G.voisins(depart):
        if not destination in vus:
            parcours_profondeur(G, destination, vus)
    return vus

def parcours_profondeur_pile(G, depart):
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = []
    à_explorer = ...
    ...
    while not ...:
        sommet = ...
        vus.append(sommet)
        # ajout des voisins non visités
        for destination in reversed(G.voisins(sommet)):
            if ...:
                ...
    return vus

class MonTableau:
    def __init__(self, tab):
        """ MonTableau, [int] -> Nonetype """
        self.contenu = tab

   class Ensemble:
       def __init__(self):
           """ Ensemble -> Nonetype """
           self.contenu = dict()

       def ajouter(self, elt):
           """ Ensemble, elt -> Nonetype """
           pass

       def supprimer(self, elt):
           """ Ensemble, elt -> Nonetype """
           pass

       def __contains__(self, elt):
           """ Ensemble, elt -> bool """
           pass

def parcours_profondeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur """
    pass

def parcours_largeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur """
    pass

